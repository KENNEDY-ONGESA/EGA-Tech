@echo off
echo Starting Music Playlist Generator...

echo --> Starting Backend (Flask)...
start "Backend" cmd /k "cd backend && python app.py"

echo --> Starting Frontend (Vue CLI)...
cd frontend
start "Frontend" cmd /k "npm run serve"

echo Services started in new windows.
