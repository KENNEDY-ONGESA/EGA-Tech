# 🎵 Music Playlist Generator

Hi! 👋 This is a project I built to learn full-stack development. It's a web app that asks an AI to create a music playlist for you based on the genre you start. I used **Vue.js** for the frontend and **Python Flask** for the backend.

---

## 🧐 What does it do?

- **Pick a Genre**: You select a genre like Pop, Jazz, or Rock.
- **AI Magic**: The app sends your choice to an AI (Hugging Face), which picks 5 songs for you.
- **Handles Errors**: If the AI is busy or breaks, I wrote code to show a backup playlist so the app doesn't crash.
- **Easy Start**: I wrote a bash script so you can start everything with just one command!

---

## 💻 Tech Stack (What I used)

### Frontend (The Visuals)

- **Vue.js 3**: I used the `<script setup>` syntax and **Composition API** to verify my logic.
- **Reactive State**: I used `ref()` variables to track the `selectedGenre`, `playlist` data, and the `loading` spinner state.
- **Simple Fetch**: I used the native `fetch` API to POST JSON data to my Flask backend at `/api/generate-playlist`.
- **Custom CSS**: I didn't use any libraries! I wrote my own **scoped CSS** using Flexbox to align the input group and results table perfectly in the center.

### Backend (The Logic)

- **Python Flask**: A simple server to handle requests.
- **Hugging Face API**: I'm using the `Qwen` model to generate the songs.
- **Regex**: I used this to clean up the messy text the AI sometimes sends back.

---

## 📂 How the code is organized

- `backend/`: All the Python code lives here.
  - `app.py`: The main server file.
- `frontend/`: The Vue.js code.
  - `src/components/PlaylistGenerator.vue`: This is where I put all the UI logic (`generatePlaylist` function) and the HTML template.
- `start.sh`: My script to automate the setup process.

---

## 🚀 How to Run It

I wanted to make it easy to run, so I made a script that does everything for you.

### Prerequisities

You need to have **Node.js** and **Python** installed on your computer.

### The Fast Way (Recommended)

Just open your terminal in this folder and run:

```bash
./start.sh
```

_(On Windows, you can just double-click `start.bat`)_

This script will automatically:

1.  Set up the Python environment.
2.  Install all the requirements.
3.  Start the Backend and Frontend at the same time!

### The Manual Way

If the script doesn't work, you can do it step-by-step:

1.  **Start the Backend:**

    ```bash
    cd backend
    python -m venv venv
    source venv/Scripts/activate  # (Or venv/bin/activate on Mac)
    pip install -r requirements.txt
    python app.py
    ```

2.  **Start the Frontend:**
    ```bash
    cd frontend
    npm install
    npm run serve
    ```

---

## ⚙️ Configuration

To get the real AI working, you need an API key.

1.  Go to `backend/`
2.  Create a file called `.env`
3.  Add your key like this:
    `    HF_TOKEN=your_token_here
   `
    _(If you don't have a key, don't worry! The app will use "Mock Data" so you can still see how it looks.)_

---

## 🐛 Challenges I Solved

- **Async/Await**: I learned how to use `async/await` in the `generatePlaylist` function to wait for the API response without freezing the button.
- **Conditional Rendering**: I used `v-if="playlist.length > 0"` so the "Your Mix" section only appears _after_ we get results.
- **Styling Forms**: It was tricky to make the `<select>` dropdown look good in dark mode, but I fixed it with custom borders and padding.

---

_Thanks for checking out my project!_
