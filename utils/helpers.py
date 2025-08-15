# Utility functions for HomeMatch application

import os
from dotenv import load_dotenv

def setup_environment():
    """
    Set up environment variables and configuration
    
    Returns:
        bool: True if setup was successful, False otherwise
    """
    # Load environment variables from .env file
    load_dotenv()
    
    # Set up OpenAI API base URL and key for Vocareum
    import openai
    
    # Set OpenAI API base URL and key
    openai.api_base = "https://openai.vocareum.com/v1"
    
    # Check if OpenAI API key is set
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("WARNING: OpenAI API key not found. Please set it in .env file.")
        return False
    
    # Set the API key
    openai.api_key = api_key
    os.environ["OPENAI_API_BASE"] = "https://openai.vocareum.com/v1"
    
    return True

def create_directory_if_not_exists(directory_path):
    """
    Create a directory if it doesn't exist
    
    Args:
        directory_path (str): Path to the directory
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Created directory: {directory_path}")

def display_listing(listing, index=None):
    """
    Display a real estate listing with formatting
    
    Args:
        listing (dict): Dictionary containing listing details
        index (int, optional): Index of the listing
    """
    if index is not None:
        print(f"Listing {index}:")
    
    print(f"Neighborhood: {listing['neighborhood']}")
    print(f"Price: {listing['price']}")
    print(f"Bedrooms: {listing['bedrooms']}")
    print(f"Bathrooms: {listing['bathrooms']}")
    print(f"House Size: {listing['house_size']}")
    print(f"Description: {listing['description']}")
    print(f"Neighborhood Description: {listing['neighborhood_description']}")
    
    if 'similarity_score' in listing:
        print(f"Similarity Score: {listing['similarity_score']:.4f}")
    
    print("-" * 80)
