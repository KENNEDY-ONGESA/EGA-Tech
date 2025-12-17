# 🎤 Presentation Day Checklist

## 1. Preparation (10 Mins Before)

- [ ] **Open 4 Tabs** in your Browser:
  1.  **Slides** (Your main deck).
  2.  **Live App** (The Netlify URL).
  3.  **GitHub Repo** (To show the code organization).
  4.  **Azure Portal** (To show the live backend resource - "Proof of Cloud").
- [ ] **Start Localhost** as Backup:
  - Run `./start.sh` just in case the internet dies. Have `localhost:8080` open in a hidden window.

## 2. The Demo Flow

1.  **The Hook**: "Who has trouble finding good music?" -> Introduce the solution.
2.  **The Architecture**: Show the slide with Frontend (Vue) -> Backend (Flask) -> AI.
3.  **The Live Demo**:
    - Select "Jazz".
    - Click Generate.
    - _Talk while it loads_: "Right now, this request is traveling to my Python backend on Azure, which is asking the Hugging Face AI model to curate a list..."
    - _Result appears_: "And there it is."
4.  **The Code Walkthrough**:
    - Show `start.sh`: "I automated the developer experience."
    - Show `app.py`: "I handled AI errors gracefully."
    - Show `.github/workflows`: "I implemented CI/CD with Azure."

## 3. Q&A "Cheat Codes"

- **Q: Why Vue.js?**
  - A: "I wanted a reactive UI framework that is lightweight and easy to integrate with a Python backend."
- **Q: How do you handle API limits?**
  - A: "I implemented a fallback mechanism. If the AI quota is hit, the system gracefully degrades to serving cached/mock data so the user never sees a crash."
- **Q: Improvements for V2?**
  - A: "I would add Spotify integration to directly save the playlist to the user's account."

## 4. Emergency Plan 🚨

- **If Netlify fails**: Switch to Localhost tab.
- **If AI fails**: Mention "The app is currently using the Fallback Data mode due to API traffic." (This makes it look like a feature, not a bug!)
