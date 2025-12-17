from flask import Flask, request, jsonify
from flask_cors import CORS
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# configurations
HF_TOKEN = os.getenv("HF_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

print(f"--> DEBUG: Current working directory: {os.getcwd()}")
print(f"--> DEBUG: HF_TOKEN from env: {'FOUND' if HF_TOKEN else 'MISSING'}")
if HF_TOKEN:
    print(f"--> DEBUG: HF_TOKEN length: {len(HF_TOKEN)}")
    print(f"--> DEBUG: HF_TOKEN prefix: {HF_TOKEN[:4]}...")

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

@app.route('/generate-playlist', methods=['POST'])
def generate_playlist():
    data = request.json
    genre = data.get('genre')

    if not genre:
        return jsonify({"error": "Genre is required"}), 400

    prompt = (
        f"You are a music expert. Create a playlist of 5 songs for the genre '{genre}'. "
        "Return the result ONLY as a JSON array of objects, where each object has 'title' and 'artist' keys. "
        "Example format: [{\"title\": \"Song Name\", \"artist\": \"Artist Name\"}]. "
        "Do not include any other text, explanation, or numbering."
    )

    try:
        text_output = ""
        if HF_TOKEN:
            try:
                # Qwen2.5-7B-Instruct is a very strong model currently active on free tier
                model_id = "Qwen/Qwen2.5-7B-Instruct" 
                print(f"Using Hugging Face with token: {HF_TOKEN[:4]}... model: {model_id}")
                client = InferenceClient(token=HF_TOKEN)
                response = client.chat_completion(
                    messages=[{"role": "user", "content": prompt}],
                    model=model_id, 
                    max_tokens=300,
                    temperature=0.7
                )
                text_output = response.choices[0].message.content
                print(f"HF Response Raw: {text_output}") # Debug print
            except Exception as hf_error:
                print(f"Hugging Face API Error: {hf_error}")
                print("Falling back to Mock Data due to API error.")
                text_output = None 
        
        # Priority 2: OpenAI (if key provided)
        elif OPENAI_API_KEY:
             # ... (OpenAI code omitted for brevity)
             pass
        else:
             text_output = None

        if not text_output and not OPENAI_API_KEY:
             # Fallback logic if API failed or no keys
             print("Returning mock data.")
             return jsonify({
                 "playlist": [
                     {"title": f"Mock Song 1 ({genre})", "artist": "Mock Artist A"},
                     {"title": f"Mock Song 2 ({genre})", "artist": "Mock Artist B"},
                     {"title": f"Mock Song 3 ({genre})", "artist": "Mock Artist C"},
                     {"title": f"Mock Song 4 ({genre})", "artist": "Mock Artist D"},
                     {"title": f"Mock Song 5 ({genre})", "artist": "Mock Artist E"},
                 ],
                 "source": "mock_fallback"
             })
             
        if text_output:
            import json
            import re
            
            songs = []
            
            def clean_and_parse_json(text):
                try:
                    # 1. Attempt extracting typical JSON array structure
                    match = re.search(r'\[.*\]', text, re.DOTALL)
                    json_str = match.group(0) if match else text
                    return json.loads(json_str)
                except json.JSONDecodeError:
                    # 2. Heuristic Fixes
                    # Sometimes quotes are missing or it's single quotes
                    try:
                        # Replace single quotes with double quotes (basic attempt)
                        fixed_str = json_str.replace("'", '"')
                        return json.loads(fixed_str)
                    except:
                        pass
                    return None

            parsed_data = clean_and_parse_json(text_output)
            
            if isinstance(parsed_data, list):
                songs = parsed_data
            else:
                # Fallback: Regex-based extraction if JSON parse fails completely
                # Looks for {"title": "X", "artist": "Y"} patterns manually
                pattern = r'\{\s*"title"\s*:\s*"(.*?)"\s*,\s*"artist"\s*:\s*"(.*?)"\s*\}'
                matches = re.findall(pattern, text_output)
                for title, artist in matches:
                    songs.append({"title": title, "artist": artist})


            # Additional cleanup/validation
            valid_songs = []
            for s in songs:
                 if isinstance(s, dict) and s.get('title') and s.get('artist'):
                     valid_songs.append(s)
            
            if not valid_songs:
                 # If everything failed, try line-by-line fallback
                 lines = text_output.strip().split('\n')
                 for line in lines:
                     if len(line) > 5 and "-" in line:
                         parts = line.split("-", 1)
                         valid_songs.append({"title": parts[0].strip(), "artist": parts[1].strip()})

            # Ensure we have at least some songs
            return jsonify({"playlist": valid_songs[:5], "source": "ai"})
            
    except Exception as e:
        print(f"CRITICAL ERROR in generate_playlist: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": "Failed to generate playlist"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
