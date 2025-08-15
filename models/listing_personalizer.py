# Listing Personalizer Module
# Responsible for personalizing listing descriptions based on buyer preferences

from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

class ListingPersonalizer:
    """
    Class for personalizing listing descriptions based on buyer preferences.
    """
    
    def __init__(self, temperature=0.5):
        """
        Initialize the ListingPersonalizer.
        
        Args:
            temperature (float): The temperature for the LLM
        """
        self.llm = OpenAI(
            temperature=temperature,
            openai_api_key=os.environ.get("OPENAI_API_KEY"),
            openai_api_base=os.environ.get("OPENAI_API_BASE", "https://openai.vocareum.com/v1")
        )
        
        # Create prompt template for personalizing descriptions
        self.personalize_template = """
        I have a home buyer with the following preferences:
        
        {preferences}
        
        Here is a real estate listing that matched their preferences:
        
        Neighborhood: {neighborhood}
        Price: {price}
        Bedrooms: {bedrooms}
        Bathrooms: {bathrooms}
        House Size: {house_size}
        
        Original Description: {description}
        
        Neighborhood Description: {neighborhood_description}
        
        Please rewrite the property description to emphasize aspects that align with the buyer's preferences.
        Make it more appealing to this specific buyer without changing any factual information about the property.
        Keep the length similar to the original description.
        
        Personalized Description:
        """
        
        # Create LLMChain for personalizing descriptions
        self.personalize_prompt = PromptTemplate(
            input_variables=["preferences", "neighborhood", "price", "bedrooms", 
                            "bathrooms", "house_size", "description", "neighborhood_description"],
            template=self.personalize_template
        )
        self.personalize_chain = LLMChain(llm=self.llm, prompt=self.personalize_prompt)
    
    def personalize_listings(self, matching_listings, buyer_preferences):
        """
        Personalize listing descriptions based on buyer preferences
        
        Args:
            matching_listings (list): List of matching listings
            buyer_preferences (list): List of buyer preference answers
            
        Returns:
            list: List of listings with personalized descriptions
        """
        # Combine buyer preferences into a single text
        preferences_text = "\n".join([f"- {pref}" for pref in buyer_preferences])
        
        # Personalize descriptions for each matching listing
        personalized_listings = []
        for listing in matching_listings:
            print(f"Personalizing description for listing in {listing['neighborhood']}...")
            
            # Generate personalized description
            personalized_description = self.personalize_chain.run(
                preferences=preferences_text,
                neighborhood=listing['neighborhood'],
                price=listing['price'],
                bedrooms=listing['bedrooms'],
                bathrooms=listing['bathrooms'],
                house_size=listing['house_size'],
                description=listing['description'],
                neighborhood_description=listing['neighborhood_description']
            )
            
            # Create a copy of the listing with personalized description
            personalized_listing = listing.copy()
            personalized_listing['original_description'] = listing['description']
            personalized_listing['personalized_description'] = personalized_description.strip()
            
            personalized_listings.append(personalized_listing)
        
        return personalized_listings
    
    def display_personalized_listings(self, personalized_listings):
        """
        Display personalized listings with their details
        
        Args:
            personalized_listings (list): List of personalized listings
        """
        print("\n=== PERSONALIZED LISTINGS ===\n")
        for i, listing in enumerate(personalized_listings):
            print(f"Personalized Match {i+1}:")
            print(f"Neighborhood: {listing['neighborhood']}")
            print(f"Price: {listing['price']}")
            print(f"Bedrooms: {listing['bedrooms']}")
            print(f"Bathrooms: {listing['bathrooms']}")
            print(f"House Size: {listing['house_size']}")
            print(f"\nORIGINAL Description: {listing['original_description']}")
            print(f"\nPERSONALIZED Description: {listing['personalized_description']}")
            print(f"\nNeighborhood Description: {listing['neighborhood_description']}")
            print("=" * 80)
