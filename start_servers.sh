#!/bin/bash

echo "Starting Market Map servers..."
echo ""

# Start the notes server in the background
echo "Starting notes server on http://localhost:5001"
python3 notes_server.py &
NOTES_PID=$!

# Wait a moment for notes server to start
sleep 2

# Start the main web server
echo "Starting web server on http://localhost:8000"
echo ""
echo "Access the website at: http://localhost:8000"
echo "Notes API running at: http://localhost:5001"
echo ""
echo "Press Ctrl+C to stop both servers"

# Function to cleanup on exit
cleanup() {
    echo ""
    echo "Stopping servers..."
    kill $NOTES_PID 2>/dev/null
    pkill -f "python3 -m http.server" 2>/dev/null
    exit 0
}

# Set up signal handlers
trap cleanup SIGINT SIGTERM

# Start the main server
python3 -m http.server 8000 