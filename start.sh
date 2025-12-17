#!/bin/bash

# Function to kill processes on exit
cleanup() {
    echo "Stopping services..."
    kill $BACKEND_PID
    kill $FRONTEND_PID
    exit
}

trap cleanup SIGINT

echo "Starting Music Playlist Generator..."

# --- BACKEND SETUP & START ---
echo "--> Setting up Backend..."
cd backend

# 1. Check if venv exists, create if not
if [ ! -d "venv" ]; then
    echo "Creating python virtual environment..."
    python -m venv venv
    
    # Activate venv (try Windows path first, then Unix)
    if [ -f "venv/Scripts/activate" ]; then
        source venv/Scripts/activate
    else
        source venv/bin/activate
    fi
    
    echo "Installing backend requirements..."
    pip install -r requirements.txt
else
    # Activate existing venv
    if [ -f "venv/Scripts/activate" ]; then
        source venv/Scripts/activate
    else
        source venv/bin/activate
    fi
fi

echo "--> Starting Flask Server..."
python app.py &
BACKEND_PID=$!
cd ..

# --- FRONTEND SETUP & START ---
echo "--> Setting up Frontend..."
cd frontend

# 2. Check if node_modules exists, install if not
if [ ! -d "node_modules" ]; then
    echo "Installing frontend dependencies (this may take a moment)..."
    npm install
fi

echo "--> Starting Vue Server..."
npm run serve &
FRONTEND_PID=$!
cd ..

echo "Both services are running!"
echo "Backend: http://localhost:5000"
echo "Frontend: http://localhost:8080"
echo "Press Ctrl+C to stop."

wait
