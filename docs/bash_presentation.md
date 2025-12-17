# 🚀 Deployment Automation: The Bash Script

## 1. The Problem

In modern web development, running a full-stack app usually requires:

1.  Opening Terminal 1 -> `cd backend` -> activating virtual env -> `python app.py`
2.  Opening Terminal 2 -> `cd frontend` -> installing npm packages -> `npm run serve`
3.  Manually killing both when done.

This is tedious and error-prone.

## 2. The Solution: `start.sh`

This script automates the entire lifecycle of the application in a single command.

## 3. Key Technical Features

### A. Cross-Platform Compatibility

The script explicitly checks which Operating System behaves like Windows or Linux when activating Python:

```bash
if [ -f "venv/Scripts/activate" ]; then
    source venv/Scripts/activate  # Windows style
else
    source venv/bin/activate      # Unix style
fi
```

This ensures the script works for every developer on the team to matter their OS.

### B. Parallel Execution (`&`)

We use the ampersand `&` to run processes in the background.

- `python app.py &` starts the Flask server but returns control immediately.
- `npm run serve &` starts the Vue server immediately after.
- **The Result:** Both servers boot up "at the same time" (concurrently).

### C. Process Management (PIDs)

We capture the **Process ID** of every background task:

```bash
BACKEND_PID=$!
FRONTEND_PID=$!
```

This serves as a handle so we can control these specific programs later.

### D. The Cleanup Trap

We use the `trap` command to listen for the `SIGINT` signal (Ctrl+C).

```bash
trap cleanup SIGINT
```

When the user tries to quit, this function triggers automatically, killing both `$BACKEND_PID` and `$FRONTEND_PID`. This prevents "zombie processes" from lingering on your computer and blocking ports 5000 or 8080.

## 4. Key Takeaway for Presentation

"This script turns a complex, multi-step startup procedure into a **single-click experience**. It handles dependencies, environment setup, parallel execution, and clean shutdown, significantly improving developer experience (DX)."
