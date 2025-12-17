# ☁️ Deploying Backend to Azure (GitHub Actions)

This guide shows you how to automate your backend deployment to Microsoft Azure using GitHub Actions.

---

## 📋 Prerequisites

1.  **Azure Account**: You need an active subscription (Free Tier works).
2.  **GitHub Repository**: Your code must be pushed to GitHub.

---

## 🛠 Step 1: Create the Azure Web App

1.  Log in to the [Azure Portal](https://portal.azure.com).
2.  Search for **"App Services"** and click **Create**.
3.  **Basics Tab**:
    - **Subscription**: Select yours.
    - **Resource Group**: Create new (e.g., `ega-project-rg`).
    - **Name**: Unique name (e.g., `ega-music-backend`).
    - **Publish**: `Code`.
    - **Runtime stack**: `Python 3.9` (or 3.10).
    - **Operating System**: `Linux` (Recommended for Python).
    - **Region**: Pick one close to you.
    - **Pricing Plan**: Select **Free F1** (or Basic B1 if you have credits).
4.  Click **Review + create** -> **Create**.

---

## 🔑 Step 2: Get the Publish Profile

This secret file allows GitHub to login to Azure without needing your username/password.

### ⚠️ Common Error: "Basic Auth Disabled"

If you click "Get publish profile" and see an error saying **"Basic Authentication is disabled"**, follow these steps to fix it:

1.  In your Azure Web App menu (left side), go to **Settings** -> **Configuration**.
2.  Click the **General settings** tab at the top.
3.  Scroll down to **Platform settings** (or look for "SCM Basic Auth Publishing Credentials").
4.  Toggle **SCM Basic Auth Publishing Credentials** to **On**.
5.  Click **Save**.
6.  Now try clicking **"Get publish profile"** on the Overview page again. It should work!

7.  It will download a file (ends in `.PublishSettings`). Keep this safe!

---

## ⚙️ Step 3: Configure GitHub Secrets

1.  Go to your **GitHub Repository**.
2.  Click **Settings** -> **Secrets and variables** -> **Actions**.
3.  Click **New repository secret**.
    - **Name**: `AZURE_WEBAPP_PUBLISH_PROFILE`
    - **Secret**: Open the `.PublishSettings` file you downloaded in Notepad, copy EVERYTHING, and paste it here.
4.  Click **Add secret**.

---

## 📝 Step 4: Configure the Workflow

I have created a workflow file for you at `.github/workflows/azure_backend.yml`. You need to edit one line:

1.  Open `.github/workflows/azure_backend.yml`.
2.  Change line 9:
    ```yaml
    AZURE_WEBAPP_NAME: your-app-name-here
    ```
    Replace `your-app-name-here` with the **actual name** of your Azure App (e.g., `ega-music-backend`).
3.  Commit and Push this change to GitHub.

---

## 🚀 Step 5: Environment Variables

Your code needs the API keys (`HF_TOKEN`) to work on Azure.

1.  Go back to **Azure Portal** -> Your App Service.
2.  On the left menu, under **Settings**, click **Environment variables** (or Configuration).
3.  Click **New application setting** (or + Add):
    - **Name**: `HF_TOKEN`
    - **Value**: (Paste your Hugging Face token)
4.  Click **Add**, then **Save**.

---

## ✅ Test It

1.  Make a small change to your `backend/` code (or just push the workflow file).
2.  Go to the **Actions** tab in GitHub.
3.  You should see the "Deploy Backend to Azure" workflow running.
4.  Once green, your backend is live at `https://<your-app-name>.azurewebsites.net`.

⚠️ **Don't forget:** Update your Frontend (Netlify) with this new URL!
