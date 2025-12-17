# Deep Dive: `backend/app.py`

This is the core entry point for the Flask backend API. It handles HTTP requests, communicates with the external AI service, and serves data to the frontend.

## 1. Imports Breakdown

```python
from flask import Flask, request, jsonify
```

- **`Flask`**: The class used to create the application instance. It acts as the central registry for routes, extensions, and configuration.
- **`request`**: A global object that lets us access incoming data (like JSON bodies sent from the frontend) for the current thread.
- **`jsonify`**: A helper function that takes a Python dictionary and converts it into a JSON response (Standard Web format) with the correct `application/json` headers.

```python
from flask_cors import CORS
```

- **`CORS` (Cross-Origin Resource Sharing)**: Security feature. By default, browsers block frontend code (running on port 5173) from talking to a backend on a different port (5000). This library whitelist our frontend to allow communication.

```python
from huggingface_hub import InferenceClient
```

- **`InferenceClient`**: The official Python wrapper for Hugging Face's API. It abstracts away the complexity of making raw HTTP requests to different models and managing authentication.

```python
import os
from dotenv import load_dotenv
```

- **`os`**: Standard Python library to interact with the Operating System (specifically to read Environment Variables).
- **`dotenv`**: Loads variables from a `.env` file into the system's environment variables, so we don't have to hardcode secrets in the script.

---

## 2. Configuration & Setup

```python
load_dotenv()
app = Flask(__name__)
CORS(app)
```

- Initializes the app and enables CORS for all routes (allowing `*` origins by default, which is fine for dev/bootcamps).

```python
HF_TOKEN = os.getenv("HF_TOKEN")
```

- Retrieves the API key securely. If this is None, the app later decides to fallback to mock data.

---

## 3. Function: `clean_and_parse_json(text)`

**Purpose**: Robustness / Sanitization.
LLMs (AI) are "probabilistic", meaning they generate text token-by-token. Even if asked for JSON, they might output:

- Extra text: _"Here is your playlist: [...]"_
- Syntax errors: Missing quotes, trailing commas.

**Logic**:

1.  **Regex Search (`re.search`)**: Instead of parsing the whole string, it looks specifically for a block starting with `[` and ending with `]`. This ignores any "Chatter" the AI adds.
2.  **`json.loads`**: Attempts standard parsing.
3.  **Heuristic Fixes**: If standard parsing fails (e.g., due to single quotes `'` which are valid in Python but invalid in JSON), it tries `replace("'", '"')` and parses again.

---

## 4. Route: `/generate-playlist`

**Method**: `POST`  
**Purpose**: The main business logic controller.

### Workflow:

1.  **Validation**:

    ```python
    data = request.json
    genre = data.get('genre')
    if not genre: ...
    ```

    Fail fast if the frontend sent an empty request.

2.  **Prompt Engineering**:

    ```python
    prompt = f"You are a music expert... Return ... JSON array..."
    ```

    We construct a specific instruction. We are being "opinionated" with the AI, forcing it to use a strict format (JSON) to make our code's job easier later.

3.  **AI Inference (The `try/except` block)**:

    - **Client Selection**: We use `Qwen/Qwen2.5-7B-Instruct` because it is a "Instruction Tuned" model (good at following rules) and available on the free tier.
    - **`chat_completion`**: We use the Chat API (Messages: User/System) because modern models are trained on dialogue, not just raw text completion.

4.  **Fallback Strategy**:

    - If the API fails (Network error, Rate limit, Bad Token), the code catches the Exception.
    - It sets `text_output = None`.
    - Later, `if not text_output`, it returns **Mock Data**. This ensures the professor/user always sees _something_ working, even if the internet is down.

5.  **Parsing & Response**:
    - It passes the raw AI text to `clean_and_parse_json`.
    - It filters the result to ensure every item has a `title` and `artist`.
    - Finally, it returns `jsonify(...)` to the frontend.
