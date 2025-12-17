# 🌐 Connecting Frontend (Netlify) to Backend (Azure)

Now that your Backend is live on Azure, we need to tell your Netlify Frontend to stop looking at `localhost` and start talking to the cloud.

---

## Step 1: Get your Backend URL

1.  Go to the **Azure Portal**.
2.  Click on your App Service (**Music-Playlist-Generator**).
3.  Copy the **Default Domain** from the Overview page.
    - It looks like: `https://music-playlist-generator.azurewebsites.net`
    - **Crucial:** Make sure it starts with `https://` and has **NO trailing slash** at the end.

---

## Step 2: Configure Netlify

1.  Log in to [app.netlify.com](https://app.netlify.com/).
2.  Click on your site (e.g., `elastic-beaver-12345`).
3.  Go to **Site configuration** (or "Site settings").
4.  On the left sidebar, click **Environment variables**.
5.  Click **Add a variable** (or "New variable").
    - **Key:** `VUE_APP_API_URL`
    - **Value:** Paste your Azure URL here (e.g., `https://music-playlist-generator.azurewebsites.net`).
    - **Scopes:** Select "Builds" and "Runtime" (or "All scopes").
6.  Click **Create variable**.

---

## Step 3: Trigger a Re-Deploy

Netlify bakes these variables into the app _during the build process_. So, even though you saved the variable, the live site won't know about it until you build it again.

1.  Go to the **Deploys** tab in the top menu.
2.  Click the **Trigger deploy** button (usually on the right side).
3.  Select **Deploy site**.

---

## Step 4: Verification

1.  Wait for the Netlify build to finish (about 1-2 minutes).
2.  Open your Netlify website URL.
3.  Open the **Developer Console** (`F12` -> Network Tab).
4.  Select a Genre and click **Generate**.
5.  Look at the network request. It should now go to `azurewebsites.net/...` instead of `localhost`.

🎉 **Congratulations!** You now have a fully deployed, cloud-native full-stack application.
