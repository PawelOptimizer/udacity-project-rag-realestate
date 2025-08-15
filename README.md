# HomeMatch: Personalized Real Estate Matching Application

## Project Overview

HomeMatch is an AI-powered real estate matching application that connects home buyers with properties tailored to their specific preferences. Using Large Language Models (LLMs) and vector databases, the application creates personalized property recommendations with descriptions that highlight the aspects most relevant to each buyer.

## Features

- **AI-Generated Listings**: Creates diverse and realistic real estate listings using LLMs
- **Vector Database Storage**: Stores listings in a vector database for semantic search
- **Preference Collection**: Gathers buyer preferences through natural language questions
- **Semantic Search**: Matches buyer preferences with relevant properties
- **Personalized Descriptions**: Tailors property descriptions to emphasize features that align with buyer preferences

## Project Structure

```
HomeMatch/
│
├── models/                # Core application modules
│   ├── listing_generator.py      # Generates real estate listings
│   ├── vector_db.py              # Manages vector database operations
│   ├── preference_manager.py     # Handles buyer preferences
│   ├── listing_personalizer.py   # Personalizes listing descriptions
│   └── home_match.py             # Main application class
│
├── utils/                 # Utility functions
│   └── helpers.py                # Helper functions
│
├── data/                  # Data storage
│   ├── listings.json             # Generated real estate listings
│   └── vectordb/                 # Vector database storage
│
├── HomeMatch.ipynb        # Jupyter notebook demonstrating the application
├── main.py                # CLI script to run the application
├── README.md              # Project documentation
├── requirements.txt       # Required dependencies
└── .env.example           # Example environment variables
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/homematch.git
cd homematch
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your-openai-api-key
```

## Usage

There are two ways to run the HomeMatch application:

### 1. Using the Jupyter Notebook

```bash
jupyter notebook HomeMatch.ipynb
```

Run through the cells to see the application in action. The notebook demonstrates each component of the system.

### 2. Using the Command Line Interface

```bash
python main.py
```

This will run the complete HomeMatch application with default settings and offer the option to run it with alternative preferences.

## Implementation Details

### Modular Architecture

The application uses an object-oriented approach with the following classes:

1. **ListingGenerator**: Generates synthetic real estate listings using OpenAI's LLM
2. **VectorDBManager**: Handles storing and retrieving listings from the vector database
3. **PreferenceManager**: Collects and processes buyer preferences
4. **ListingPersonalizer**: Personalizes listing descriptions based on preferences
5. **HomeMatch**: Coordinates all components and provides a simple interface

## Installation

### Quick Setup

For your convenience, this project includes setup scripts that automatically create a virtual environment and install all required dependencies:

#### For macOS/Linux:
```bash
chmod +x setup.sh
./setup.sh
```

### Manual Setup

1. Create a virtual environment:
```bash
# For macOS/Linux
python -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up Jupyter kernel:
```bash
pip install ipykernel
python -m ipykernel install --user --name=homematch --display-name="HomeMatch"
```

4. Set your OpenAI API key in a `.env` file:
```
OPENAI_API_KEY=your-api-key-here
```

For detailed setup instructions, see the `SETUP.md` file.

## Project Components

### 1. Listing Generation

The application uses OpenAI's LLM to generate synthetic real estate listings with:
- Neighborhood information
- Price
- Number of bedrooms and bathrooms
- House size
- Detailed property description
- Neighborhood description

### 2. Vector Database

Listings are stored in ChromaDB, a vector database that enables semantic search:
- Each listing is converted to embeddings that capture semantic meaning
- Embeddings are stored for efficient similarity search
- Allows for finding properties based on meaning, not just keywords

### 3. Buyer Preferences

The application collects buyer preferences through a set of questions about:
- Desired house size
- Important features
- Amenities
- Transportation options
- Neighborhood characteristics

### 4. Semantic Search

The application converts buyer preferences into embeddings and searches the vector database for matching properties:
- Combines all preferences into a single query
- Finds properties with similar semantic meanings
- Ranks results by relevance

### 5. Personalization

For each matching property, the application generates a personalized description that:
- Emphasizes aspects that align with the buyer's preferences
- Maintains factual integrity of the original listing
- Makes the property more appealing to the specific buyer

