#!/bin/bash
set -eo pipefail

PID_DIR=pids
LOG_DIR=logs
mkdir -p "$PID_DIR" "$LOG_DIR"

stop_processes() {
  if [ -f "$PID_DIR/backend.pid" ]; then
    kill "$(cat "$PID_DIR/backend.pid")" || true
    rm -f "$PID_DIR/backend.pid"
  fi
  if [ -f "$PID_DIR/frontend.pid" ]; then
    kill "$(cat "$PID_DIR/frontend.pid")" || true
    rm -f "$PID_DIR/frontend.pid"
  fi
}

stop_processes

echo "Starting backend..."
# Placeholder backend command
python -m http.server 8000 &>"$LOG_DIR/backend.log" &
echo $! >"$PID_DIR/backend.pid"

echo "Starting frontend..."
# Placeholder frontend command
python -m http.server 3000 &>"$LOG_DIR/frontend.log" &
echo $! >"$PID_DIR/frontend.pid"

echo "Backend running at http://localhost:8000"
echo "Frontend running at http://localhost:3000"
