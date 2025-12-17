# 🚑 Troubleshooting: "Deployment Failed (403)"

The error **"HTTP status code 403"** or **"Failed to get app runtime OS"** means GitHub tried to upload your code, but Azure rejected the key (Publish Profile).

This happens because when you toggled **"Basic Auth"** to On, **Azure generated a NEW password** for your app. The old file you uploaded to GitHub is now invalid.

---

## 🛠 The Fix: Update the Secret (Must Do!)

### 1. Re-Download the Keys

1.  Go to **Azure Portal** -> Your App Service (**Music-Playlist-Generator**).
2.  Go to the **Overview** page.
3.  Click **Get publish profile** to download a **NEW** `.PublishSettings` file.
    - _(Delete the old one from your downloads folder so you don't get confused)_.

### 2. Update GitHub

1.  Go to your **GitHub Repository** -> **Settings** -> **Secrets and variables** -> **Actions**.
2.  Find `AZURE_WEBAPP_PUBLISH_PROFILE`.
3.  Click the **Pencil Icon** (Edit).
4.  **Delete everything** in the box.
5.  Open the **NEW** file you just downloaded, copy all the text, and paste it in.
6.  Click **Update Secret**.

### 3. Re-Run the Deployment

1.  Go to the **Actions** tab in GitHub.
2.  Click on the failed workflow **"Deploy Backend to Azure"** (on the left).
3.  Click the **Re-run jobs** button (top right).

---

## 🔍 Double Check: Public Access

If it _still_ fails after updating the secret, check this:

1.  Go to **Azure Portal** -> **Settings** -> **Networking**.
2.  Under **"Inbound Traffic"**, click **"Public network access"**.
3.  Make sure **"Enabled from all networks"** is selected.
4.  If you changed it, click **Save**.
