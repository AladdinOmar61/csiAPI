#!/bin/bash

# Python virt_env
echo "Activating virtual environment..."
python3 -m venv virt_env
source virt_env/bin/activate 

# Install pip packages
echo "Installing pip packages..."
pip install -r "./req.txt" # Make sure to change this before running

echo "Deactivating virtual environment..."
deactivate

#create a .env file for environment variables
touch .env