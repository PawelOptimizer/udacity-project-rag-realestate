# Listing Generator Module
# Responsible for generating real estate listings using LLM

import os
import json
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

class ListingGenerator:
    """
    Class for generating real estate listings using OpenAI's LLM.
    """
    
    def __init__(self, temperature=0.7):
        """
        Initialize the ListingGenerator.
        
        Args:
            temperature (float): The temperature for the LLM
        """
        self.llm = OpenAI(
            temperature=temperature,
            openai_api_key=os.environ.get("OPENAI_API_KEY"),
            openai_api_base=os.environ.get("OPENAI_API_BASE", "https://openai.vocareum.com/v1")
        )
        
        # Create prompt template for generating listings
        self.listing_template = """
        Generate a detailed real estate listing with the following information:
        
        1. Neighborhood: (Choose a diverse neighborhood name)
        2. Price: (Random price between $300,000 and $1,500,000)
        3. Bedrooms: (Between 1 and 5)
        4. Bathrooms: (Between 1 and 4)
        5. House Size: (Between 800 and 4,000 sqft)
        6. Description: (Detailed 4-6 sentence description of the property highlighting unique features)
        7. Neighborhood Description: (3-4 sentences about the neighborhood, amenities, and character)
        
        Make sure the listing is realistic, diverse, and follows this format:
        
        Neighborhood: [Neighborhood Name]
        Price: $[Price]
        Bedrooms: [Number]
        Bathrooms: [Number]
        House Size: [Size] sqft
        
        Description: [Detailed description of the property]
        
        Neighborhood Description: [Description of the neighborhood]
        
        Please generate this as a unique property with its own character and features. Create a property that would be number {number} in your varied portfolio.
        """
        
        self.listing_prompt = PromptTemplate(
            input_variables=["number"],
            template=self.listing_template
        )
        self.listing_chain = LLMChain(llm=self.llm, prompt=self.listing_prompt)
    
    def generate_listings(self, num_listings=10):
        """
        Generate synthetic real estate listings using OpenAI's LLM
        
        Args:
            num_listings (int): Number of listings to generate
            
        Returns:
            list: List of dictionaries containing property listings
        """
        # Generate listings
        listings = []
        for i in range(1, num_listings + 1):
            print(f"Generating listing {i}/{num_listings}...")
            response = self.listing_chain.run(number=i)
            
            # Process the generated listing
            listings.append(response.strip())
        
        # Parse listings into structured format
        structured_listings = []
        for listing in listings:
            try:
                # Extract components using parsing logic
                parts = listing.split('\n\n')
                
                # Parse the property details section
                details = {}
                for line in parts[0].split('\n'):
                    if ':' in line:
                        key, value = line.split(':', 1)
                        details[key.strip()] = value.strip()
                
                # Get description and neighborhood description
                description = ""
                neighborhood_desc = ""
                
                for part in parts[1:]:
                    if part.startswith("Description:"):
                        description = part.replace("Description:", "").strip()
                    elif part.startswith("Neighborhood Description:"):
                        neighborhood_desc = part.replace("Neighborhood Description:", "").strip()
                
                # Create structured listing
                structured_listing = {
                    'neighborhood': details.get('Neighborhood', ''),
                    'price': details.get('Price', ''),
                    'bedrooms': details.get('Bedrooms', ''),
                    'bathrooms': details.get('Bathrooms', ''),
                    'house_size': details.get('House Size', ''),
                    'description': description,
                    'neighborhood_description': neighborhood_desc
                }
                
                structured_listings.append(structured_listing)
            except Exception as e:
                print(f"Error parsing listing: {e}")
                print(f"Problematic listing: {listing}")
        
        return structured_listings
    
    def save_listings_to_file(self, listings, file_path):
        """
        Save listings to a JSON file
        
        Args:
            listings (list): List of listing dictionaries
            file_path (str): Path to save the listings
        """
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Save listings to file
        with open(file_path, 'w') as f:
            json.dump(listings, f, indent=4)
        
        print(f"All {len(listings)} listings saved to '{file_path}'")
    
    def load_listings_from_file(self, file_path):
        """
        Load listings from a JSON file
        
        Args:
            file_path (str): Path to the listings file
            
        Returns:
            list: List of listing dictionaries
        """
        with open(file_path, 'r') as f:
            listings = json.load(f)
        
        print(f"Loaded {len(listings)} listings from '{file_path}'")
        return listings
