# 🚨 CRITICAL FIX: "HTTP 403" / "Failed to get app runtime OS"

This error confirms **GitHub cannot log in** to your Azure App.
This happens for one of two specific reasons. Please check both.

---

## 🔍 Fix 1: The "SCM" Switch (Most Likely)

Azure has **two** switches for Basic Auth. You might have turned on the wrong one, or only one of them.

1.  Go to **Azure Portal** -> **Music-Playlist-Generator**.
2.  Left Menu: **Settings** -> **Configuration**.
3.  Top Tab: **General settings**.
4.  Scroll down to **Platform settings**.
5.  Look for these **TWO** checkboxes:
    - [x] **FTP Basic Auth Publishing Credentials** <-- Set to **ON**
    - [x] **SCM Basic Auth Publishing Credentials** <-- Set to **ON** (Crucial one!)
6.  If you changed anything, click **Save**.

---

## 🔑 Fix 2: The Secret Rotation (Required if you did Fix 1)

**Resetting those switches changes your password.** Your old file is useless now.

1.  Go to **Overview** (Left Menu).
2.  Click **Get publish profile** (Download the NEW file).
3.  Open the file in Notepad. **Select All** -> **Copy**.
4.  Go to **GitHub Repo** -> **Settings** -> **Secrets and variables** -> **Actions**.
5.  **Edit** `AZURE_WEBAPP_PUBLISH_PROFILE`.
6.  **Delete everything** currently there.
7.  **Paste** the NEW content.
8.  Click **Update Secret**.

---

## 🌐 Fix 3: Network Blocking (The "403" Message)

The error says "networking features enabled which are blocking access". This means the public door might be closed.

1.  Go to **Azure Portal** -> **Music-Playlist-Generator**.
2.  Left Menu: **Settings** -> **Networking**.
3.  Click **"Public network access"** (Under Inbound Traffic).
4.  Ensure **"Enabled from all networks"** is selected.
    - _Note: If it says "Disabled", GitHub is blocked._
5.  Click **Save**.

---

## 🔄 Final Step

1.  Go to **GitHub Actions**.
2.  Click the failed run.
3.  Click **Re-run jobs**.
