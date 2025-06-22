#!/bin/bash
# Simple script to install Python and Node dependencies
set -e

# Install Python dependencies
if [ -f backend/requirements.txt ]; then
    echo "Installing Python dependencies..."
    python3 -m pip install --upgrade pip
    pip install -r backend/requirements.txt
fi

# Install Node dependencies at project root (if package.json exists)
if [ -f package.json ]; then
    echo "Installing root Node dependencies..."
    npm install
fi

# Install frontend Node dependencies
if [ -d frontend ] && [ -f frontend/package.json ]; then
    echo "Installing frontend Node dependencies..."
    (cd frontend && npm install)
fi

echo "All dependencies installed."
