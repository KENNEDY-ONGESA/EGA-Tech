# 🔄 RESET GUIDE: Back to GitHub Actions

You asked to undo the manual changes and go back to the original GitHub Actions setup. Here is how to clean up the "Local Git" mess and restore the automation.

---

## 1. Reset Azure Deployment Center

We need to tell Azure to stop listening for "Local Git" and start listening to GitHub Actions again.

1.  Go to **Azure Portal** -> **Music-Playlist-Generator**.
2.  Left Menu: **Deployment** -> **Deployment Center**.
3.  **Settings** Tab:
    - **Source**: Change it to **GitHub**.
    - **Signed in as**: Ensure your GitHub account is connected.
    - **Organization**: `KENNEDY-ONGESA`.
    - **Repository**: `EGA-Tech`.
    - **Branch**: `main`.
4.  Click **Save**.

---

## 2. Verify Credentials (One Last Time)

Since we played with passwords, ensure the GitHub Secret matches the current Azure state.

1.  In **Deployment Center** (or Overview), click **Manage publish profile** (or Get publish profile).
2.  Download the file.
3.  Go to **GitHub Repo** -> Settings -> Secrets -> Actions.
4.  Update `AZURE_WEBAPP_PUBLISH_PROFILE` with the content of that file.

---

## 3. Push the Fix

I have restored your `azure_backend.yml` file to its original state. Now, just push it to trigger the build.

1.  Open Terminal.
2.  Run:

    ```bash
    git add .
    git commit -m "Restore GitHub Actions workflow"
    git push
    ```

3.  Go to the **Actions** tab in GitHub and watch it turn Green! 🟢
