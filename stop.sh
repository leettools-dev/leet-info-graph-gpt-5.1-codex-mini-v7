#!/bin/bash
set -eo pipefail

PID_DIR=pids
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

echo "Stopped backend and frontend services."
