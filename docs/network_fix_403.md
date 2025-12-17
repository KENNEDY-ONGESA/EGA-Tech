# 🛑 THE PROBLEM: "403" on Git Push

A `403` error when running `git push azure` means the **Firewall is blocking you**. Your laptop is not allowed to talk to Azure.

## 🛠 THE FIX: Open the Network

You must explicitly allow traffic from the internet.

1.  Go to **Azure Portal** -> **Music-Playlist-Generator**.
2.  Left Menu: **Settings** -> **Networking**.
3.  Look for **"Inbound traffic"**.
4.  Click **"Public network access"**.
5.  **Status**: Must be set to **"Enabled from all networks"**.
    - _If it is set to "Disabled" or "Selected networks", you will ALWAYS get a 403._
6.  Click **Save**.

---

## 🔍 Double Check: The SCM Switch

If Networking is already Enabled, then the "Login Key" switch is still off.

1.  Left Menu: **Configuration**.
2.  Top Tab: **General settings**.
3.  **SCM Basic Auth Publishing Credentials**: Make sure it is **ON**.
    - _(Note: There are TWO switches. One for FTP, one for SCM. You need SCM)._
4.  Click **Save**.

---

## 🔄 Try Again

Once "Public Network" is Enabled and "SCM Auth" is On:

1.  Close your terminal.
2.  Open a new terminal.
3.  Run:
    ```bash
    git push azure main
    ```
