# Clean & Modular Code Architecture

Your project follows the **"Separation of Concerns"** principle, which is the heart of modular code. Instead of one giant file doing everything, we split the logic into distinct layers.

## 1. Backend Modularity (The Logical Split)

In the `backend` folder, we didn't just dump everything into `app.py`.

- **Logic Isolation**: We separated the **Configuration** (`.env`, `load_dotenv`) from the **Application Logic** (`app.py`).
  - _Why?_ If you change your API key, you don't risk breaking the Python code.
- **Helper Functions**:
  - **`clean_and_parse_json()`**: We extracted the complex logic of fixing broken JSON into its own function.
  - _Why?_ It keeps the main route handler (`generate_playlist`) clean and readable. You can read the main logic flow ("Get Genre -> Call AI -> Parse -> Return") without being distracted by 20 lines of messy Regex code.

## 2. Frontend Component-Based Architecture (The Vue Way)

Vue.js is designed to be modular.

- **Components (`src/components/`)**:
  - We created `PlaylistGenerator.vue`.
  - _Why?_ If you wanted to add this playlist feature to a different page (e.g., an "About" page), you could just drop `<PlaylistGenerator />` there. You wouldn't have to copy-paste 200 lines of code. It acts like a reusable LEGO block.
- **Services (`api` proxy)**:
  - We configured `vite.config.js` to handle the proxy (`/api` -> `localhost:5000`).
  - _Why?_ The frontend code doesn't hardcode `http://localhost:5000`. It just calls `/api`. This means if you deploy the backend to a real server (like Heroku) later, you only change the config in ONE place, not in every single file.

## 3. Atomic styling

- **Scoped CSS**: inside `PlaylistGenerator.vue`, we used `<style scoped>`.
  - _Why?_ This ensures the styles for the card don't accidentally break the styles for the rest of the website. It modules the visual design.

---

## checklist for your presentation

If the assessors ask "How is this modular?", answer:

1.  **Frontend/Backend Split**: They are two completely separate projects that talk via a standard Interface (JSON API).
2.  **Component Reuse**: The UI logic is encapsulated in a single file component (`.vue`).
3.  **Encapsulation**: Helper functions (like JSON parsing) are extracted to keep the main code paths simple.
