# Deep Dive: Startup Scripts (`start.sh` & `start.bat`)

These scripts are "Helpers". Their only job is to save you from opening two separate terminal windows and typing commands manually every time you want to work on your project.

---

## 1. `start.sh` (The Bash Script)

**Target OS:** Linux, macOS, Git Bash on Windows.

### The Shebang

```bash
#!/bin/bash
```

- This first line tells the computer: "Hey, use the **Bash** program to run the rest of this file."

### The Cleanup Function (Signal Handling)

```bash
cleanup() {
    echo "Stopping services..."
    kill $BACKEND_PID
    kill $FRONTEND_PID
    exit
}

trap cleanup SIGINT
```

- **The Problem**: If you start two background programs and then just close the window, those programs might keep running secretly in the background (Zombie processes!).
- **`trap cleanup SIGINT`**: This is a trap. It says, "If the user presses `Ctrl+C` (which sends a **SIGINT** signal), DO NOT just quit immediately. Run the `cleanup` function first."
- **`cleanup`**: This function finds the Process IDs (PIDs) we saved earlier and kills them specifically, ensuring a clean exit.

### Starting Processes in Background (`&`)

```bash
python app.py &
BACKEND_PID=$!
```

- **`&` (Ampersand)**: This is crucial. Normally, if you run `python app.py`, the terminal waits forever until Python stops. Adding `&` tells Bash: "Run this in the background and give me back control of the terminal immediately."
- **`$!`**: This special variable holds the **Process ID (PID)** of the last command we ran in the background. We save it into `BACKEND_PID` so the cleanup function knows exactly _what_ to kill later.

### The Wait

```bash
wait
```

- Since both Python and Node are running in the background, the script would normally reach the end of the file and exit immediately. `wait` tells the script: "Pause here and don't exit until the background processes finish." This keeps the script alive so it can listen for your `Ctrl+C`.

---

## 2. `start.bat` (The Windows Batch Script)

**Target OS:** Windows (Command Prompt).

### Hiding Clutter

```cmd
@echo off
```

- By default, Windows prints every command it executes. `@echo off` tells it: "Don't show the commands themselves, only show the output (like my logs)."

### The `start` Command

```cmd
start "Backend" cmd /k "cd backend && python app.py"
```

- **`start "Backend"`**: This opens a **new popup window** and titles it "Backend". This is different from the Bash script which runs everything in _one_ window. Windows handles background tasks differently, so separate windows are often cleaner for dev.
- **`cmd /k`**: This tells the new window: "Run this command and **K**eep the window open afterwards." (If you returned `/c`, it would Close immediately if the program crashed, making it hard to read errors).
- **`cd backend && python app.py`**:
  1.  Change directory to `backend`.
  2.  **`&&`**: Run the next command ONLY if the first one succeeded.
  3.  Run the python app.

### Why do we need both?

- Developers use different computers.
- **`start.sh`** is standard for servers and Mac/Linux developers.
- **`start.bat`** is standard for Windows developers who just want to double-click an icon.
- By including both, your project is "Cross-Platform Friendly."
