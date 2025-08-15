# Setting Up the HomeMatch Project

This guide will help you set up the HomeMatch project environment.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git (optional, for version control)

## Setup Instructions

### For macOS/Linux Users:

1. **Clone or download the repository** (if not already done)

2. **Navigate to the project directory**:
   ```bash
   cd /path/to/HomeMatch
   ```

3. **Run the setup script**:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

4. **Activate the virtual environment**:
   ```bash
   source venv/bin/activate
   ```

5. **Set your OpenAI API key**:
   - Edit the `.env` file created during setup
   - Add your OpenAI API key: `OPENAI_API_KEY=your-api-key-here`

6. **Run Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

7. **Open the HomeMatch.ipynb notebook and select the "HomeMatch" kernel**

## Manual Setup (Alternative)

If the setup scripts don't work for you, follow these manual steps:

1. **Create a virtual environment**:
   ```bash
   # For macOS/Linux
   python -m venv venv
   source venv/bin/activate
   
   # For Windows
   python -m venv venv
   venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. **Set up Jupyter kernel**:
   ```bash
   pip install ipykernel
   python -m ipykernel install --user --name=homematch --display-name="HomeMatch"
   ```

4. **Create a .env file**:
   ```bash
   # Copy the example file
   cp .env.example .env
   # Then edit the .env file to add your OpenAI API key
   ```

## Troubleshooting

- **Permission denied when running setup.sh**:
  Make sure the script is executable: `chmod +x setup.sh`

- **Virtual environment not activating**:
  Ensure you're using the correct activation command for your shell

- **Package installation errors**:
  Try updating pip first: `pip install --upgrade pip`

- **Jupyter kernel not appearing**:
  Restart Jupyter after installing the kernel

- **OpenAI API errors**:
  Ensure your API key is correctly set in the .env file
