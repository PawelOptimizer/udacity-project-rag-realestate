#!/bin/bash
# HomeMatch Virtual Environment Setup Script
# This script sets up a virtual environment and installs all required packages
# for the HomeMatch project.

# Ensure we're in the project directory
cd "$(dirname "$0")"
PROJECT_DIR=$(pwd)
echo "Setting up HomeMatch virtual environment in: $PROJECT_DIR"

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install required packages
echo "Installing required packages..."
pip install -r requirements.txt

# Set up Jupyter kernel for the virtual environment
echo "Setting up Jupyter kernel..."
pip install ipykernel
python -m ipykernel install --user --name=homematch --display-name="HomeMatch"

# Create a .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file..."
    cp .env.example .env
    echo "Please update the .env file with your OpenAI API key."
fi

echo "Virtual environment setup complete!"
echo ""
echo "To activate the virtual environment, run:"
echo "    source venv/bin/activate"
echo ""
echo "To use the environment in Jupyter Notebook:"
echo "    1. Start Jupyter: jupyter notebook"
echo "    2. Open HomeMatch.ipynb"
echo "    3. Select Kernel > Change kernel > HomeMatch"
echo ""
echo "When you're done, you can deactivate the environment with:"
echo "    deactivate"
