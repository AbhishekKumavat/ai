#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

echo "Starting build process..."

# Install Python dependencies
echo "Installing Python dependencies..."
cd ..
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install -r requirements.txt

# Go back to frontend and build
echo "Building frontend..."
cd frontend
npm install
npm run build

echo "Build completed successfully!"