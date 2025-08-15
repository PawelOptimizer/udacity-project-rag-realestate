#!/bin/bash
# Fix Jupyter Kernel Issues Script
# Run this script if you have issues with the Jupyter kernel

echo "Fixing Jupyter kernel setup..."

# Get the Python executable path in the virtual environment
if [ -d "venv" ]; then
    PYTHON_PATH="venv/bin/python"
elif [ -d ".venv" ]; then
    PYTHON_PATH=".venv/bin/python"
else
    echo "No virtual environment found. Creating one..."
    python3 -m venv .venv
    PYTHON_PATH=".venv/bin/python"
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
fi

# Make sure ipykernel is installed
echo "Installing ipykernel..."
$PYTHON_PATH -m pip install ipykernel --upgrade

# Uninstall existing kernel if it exists
echo "Removing old kernel registrations if they exist..."
jupyter kernelspec uninstall homematch -y 2>/dev/null || true

# Register the kernel
echo "Registering the HomeMatch kernel..."
$PYTHON_PATH -m ipykernel install --user --name=homematch --display-name="HomeMatch"

echo "Kernel setup complete!"
echo ""
echo "To use the kernel in Jupyter Notebook:"
echo "  1. Restart Jupyter: jupyter notebook"
echo "  2. Open HomeMatch.ipynb"
echo "  3. Select Kernel > Change kernel > HomeMatch"
echo ""
