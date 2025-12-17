# 🛑 THE FINAL CHECKLIST: Why 403 Persists

A persistent `403` with "Local Git" means the door is shut. It is not a password issue (that would be 401). **403 means "Forbidden" (Blocked).**

Please check these 3 screens in Azure Portal. One of them is definitely WRONG.

---

## 📸 SCREEN 1: Networking (The Firewall)

1.  Go to **Settings** -> **Networking**.
2.  Look at **"Inbound Traffic"**.
3.  Click **"Public network access"**.
4.  **IT MUST SAY:** `Enabled from all networks`.
    - _If it says "Disabled", you are blocked._

---

## 📸 SCREEN 2: SCM Basic Auth (The Login Permission)

1.  Go to **Settings** -> **Configuration**.
2.  Click **General settings** tab.
3.  Scroll down to **Platform settings**.
4.  **SCM Basic Auth Publishing Credentials**: Switch to **ON**.
    - _If this is OFF, you are blocked._

---

## 📸 SCREEN 3: The Deployment Source (The Listener)

1.  Go to **Deployment** -> **Deployment Center**.
2.  Look at **Settings**.
3.  **Source**: Must be **Local Git**.
    - _If it is set to "GitHub" or "None", Azure is not listening for your push._

---

## 💡 If all above are correct...

It might be your **Office Network / VPN**.

- Are you on a strict corporate VPN? (e.g., Bboxx VPN?)
- Try tethering to your **Mobile Hotspot** for 1 minute and running `force_push.bat` again. Azure blocks some corporate IPs.
