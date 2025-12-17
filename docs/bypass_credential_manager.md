# 🔓 THE ULTIMATE BYPASS: Embedding Credentials

Since you are getting a `403` immediately without it asking for a password, **Windows is remembering an old, wrong password** and sending it automatically.

We will bypass Windows entirely by putting the username and password **directly into the URL**.

---

## Step 1: Get Your Secrets

1.  Go to **Azure Portal** -> **Deployment Center**.
2.  Click **Local Git/FTPS credentials**.
3.  **User Scope**:
    - **Username**: Write it down (e.g., `mydeployuser`).
    - **Password**: Write it down (e.g., `MySecretPass123!`).
    - _(If you don't know it, reset it right now and click Save)._

## Step 2: Get the Link

1.  Go to the **Settings** tab in Deployment Center.
2.  Copy the **Git Clone Uri**.
    - It looks like: `https://music-playlist-generator.scm.azurewebsites.net:443/music-playlist-generator.git`

## Step 3: Construct the "Super Link"

Combine them like this:
`https://<USERNAME>:<PASSWORD>@<THE_REST_OF_THE_LINK>`

**Example:**

- **User:** `deploy`
- **Pass:** `pass123`
- **Link:** `https://music-playlist.scm.azure...`

**Result:**
`https://deploy:pass123@music-playlist.scm.azurewebsites.net:443/music-playlist-generator.git`

---

## Step 4: The Final Push

1.  Open your terminal.
2.  Remove the failing remote:
    ```bash
    git remote remove azure
    ```
3.  Add the **Super Link** (Replace with YOUR details):
    ```bash
    git remote add azure https://USERNAME:PASSWORD@music-playlist-generator-g6freydyc6bhdye2.scm.canadacentral-01.azurewebsites.net:443/Music-Playlist-Generator.git
    ```
4.  Push:
    ```bash
    git push azure main --force
    ```

**Why this works:** It forces Git to use the password you typed in the link, ignoring whatever junk Windows Credential Manager is holding onto.
