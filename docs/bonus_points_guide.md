# 🌟 Bonus Points Guide: Deployment & Testing

This guide will help you secure those extra marks for **Netlify Hosting** and **Postman Testing**.

---

## 🚀 Part 1: Hosting on Netlify (Frontend)

Since your frontend is built with Vue, we can host it for free on Netlify!

### Step 1: Create the Production Build

By default, your code is in "development mode". We need to turn it into optimized HTML/CSS/JS files for the internet.

1.  Open your terminal.
2.  Navigate to the frontend folder:
    ```bash
    cd frontend
    ```
3.  Run the build command:
    ```bash
    npm run build
    ```
4.  **Wait** for it to finish. You should see a green "Build complete" message.
5.  Look in your project folder. You will now see a new folder named **`dist`**. This contains your deployable website.

### Step 2: Deploy to Netlify

1.  Go to [app.netlify.com](https://app.netlify.com/).
2.  Log in (or sign up with GitHub/Email).
3.  Once logged in, go to the **"Sites"** tab.
4.  Look for the area that says **"Drag and drop your site output folder here"**.
5.  Open your file explorer (`Windows Key + E`).
6.  Navigate to `c:\Users\bboxx\Vue Project\EGA Tech\frontend`.
7.  **Drag the `dist` folder** and drop it right into the Netlify browser window.

### Step 3: Verify

- Netlify will verify the files and give you a random URL (like `starlit-pudding-12345.netlify.app`).
- Click the link! Your UI is now live on the internet. 🎉

### ⚠️ Important Note about the Backend

Your backend (Flask) is running on your **laptop** (`localhost:5000`). Your Netlify site is on the **internet**.

- **The Problem:** The Netlify site cannot "see" your laptop. If you click "Generate" on the Netlify site, it might fail or give an error.
- **The Presentation Explanation:** "I have successfully deployed the frontend UI to the cloud (Netlify). For security and cost reasons, the backend AI logic currently remains on a distinct secure local server for this demo."
- **This still counts for the bonus!** You proved you can host the static asset.

---

## 📮 Part 2: Demonstrating API with Postman

If you need to show "Proof of API" in your presentation slides, follow this workflow:

1.  **Start your Backend** (using `./start.sh` or just `python app.py`).
2.  Open **Postman**.
3.  Create a new **POST** request.
4.  **URL:** `http://localhost:5000/generate-playlist`
5.  **Body Tab:**
    - Select **raw**.
    - Select **JSON** from the dropdown (instead of Text).
    - Enter this JSON:
      ```json
      {
        "genre": "Jazz"
      }
      ```
6.  Click **Send**.
7.  **Take a Screenshot** 📸 of the JSON response (the list of songs) appearing at the bottom.
8.  Paste this screenshot into your presentation as verification that your Backend API works independently of the frontend.

---

# ☁️ Bonus Part 3: Full Cloud Deployment (GitHub + Netlify + Render)

Since your code is on **GitHub**, we can connect it directly to cloud services. This allows the Netlify (Frontend) to talk to a real live Backend!

## 🏗 Step 1: Deploy the Backend (Render.com)

Netlify only hosts static websites (frontend). For the Python backend, we use **Render** (it has a great free tier).

1.  **Push your code** to GitHub (ensure `requirements.txt` has `gunicorn` - I just added it for you!).
2.  Go to [dashboard.render.com](https://dashboard.render.com/) and sign up with GitHub.
3.  Click **New +** -> **Web Service**.
4.  Select your Repository.
5.  **Settings**:
    - **Name**: `ega-music-backend` (or similar)
    - **Root Directory**: `backend` <-- IMPORTANT!
    - **Environment**: `Python 3`
    - **Build Command**: `pip install -r requirements.txt`
    - **Start Command**: `gunicorn app:app`
6.  **Environment Variables** (Add these in the "Advanced" section):
    - `HF_TOKEN`: (Your Hugging Face Token)
    - `PYTHON_VERSION`: `3.9.0` (Optional, good for stability)
7.  Click **Create Web Service**.
8.  Wait for it to deploy. Once green, copy the URL (e.g., `https://ega-music-backend.onrender.com`).

## � Step 2: Deploy the Frontend (Netlify)

Now we tell Netlify where the backend lives.

1.  Go to [app.netlify.com](https://app.netlify.com/).
2.  Click **"Add new site"** -> **"Import from existing project"**.
3.  Select **GitHub**.
4.  Pick your repository.
5.  **Build Settings**:
    - **Base directory**: `frontend`
    - **Build command**: `npm run build`
    - **Publish directory**: `frontend/dist`
6.  **Environment Variables** (Click "Show advanced" or go to Site Settings later):
    - Key: `VUE_APP_API_URL`
    - Value: `https://ega-music-backend.onrender.com` (The URL you got from Render, **without** the trailing slash `/`)
7.  Click **Deploy Site**.

## ✅ Step 3: Verify

1.  Open your new Netlify URL.
2.  Select a Genre and click **Generate**.
3.  The request will now go to your Render Backend and return real results!

---

## ❓ FAQ for Presentation

**Q: "Why are there two different URLs?"**
**A:** "This is a **Microservices Architecture**. The Frontend is decoupled and hosted on a CDN (Netlify) for speed, while the Backend API runs on a dedicated application server (Render). This allows them to scale independently."
