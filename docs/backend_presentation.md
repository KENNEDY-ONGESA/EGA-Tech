# 🧠 Backend Architecture: Flask + AI

## 1. Overview

The backend is a lightweight **Python Flask** server that acts as the bridge between the user and the Large Language Model (LLM). It handles API requests, prompts the AI, and ensures strictly formatted JSON output.

## 2. Server Structure (`app.py`)

### A. Configuration & Security

- **Environment Variables:** We use `python-dotenv` to load sensitive keys (like `HF_TOKEN`) safely from a `.env` file. This prevents hardcoding secrets.
- **CORS:** `flask_cors` is enabled to allow the Frontend (running on port 8080) to talk to this Backend (running on port 5000) without browser security errors.

### B. The AI Integration strategy

We use a **Multi-Tiered Approach** for reliability:

1.  **Primary:** **Hugging Face Inference API**. We primarily use the `Qwen/Qwen2.5-7B-Instruct` model. It is high-performance and currently free-tier friendly.
2.  **Secondary:** **OpenAI API**. (Optional) If an OpenAI key is present, it can serve as a backup.
3.  **Fallback:** **Hardcoded Mock Data**. If _everything_ fails (internet down, API limits), the system returns a pre-defined list of mock songs so the app never crashes during a demo.

### C. The `generate_playlist` Logic

This function is the brain of the application.

1.  **Prompt Engineering:** We construct a strict prompt telling the AI: _"Return the result ONLY as a JSON array... Do not include other text."_
2.  **API Call:** We send this prompt to the model via the `huggingface_hub` client.
3.  **Data Cleaning (The Helper Function):** AI often chatters (e.g., "Here is your list: [ ... ]"). We use:
    - **Regex (`re`):** To hunt down the specific `[` ... `]` JSON block within the response.
    - **JSON Parse:** We convert that text string into a real Python list/dictionary.
    - **Heuristics:** If the AI uses single quotes `'` instead of double quotes `"`, we try to fix it automatically.

### D. The API Endpoint

- **Route:** `/generate-playlist` (POST)
- **Input:** `{"genre": "Jazz"}`
- **Output:** `{"playlist": [{"title": "...", "artist": "..."}]}`

## 3. Key Takeaway for Presentation

"The backend is built for **Robustness**. We assume the external AI API might fail or return messy data. Therefore, we wrappd the AI logic in multiple layers of error handling, regex parsers, and fallbacks. The goal is that the user _always_ gets a playlist, no matter what."
