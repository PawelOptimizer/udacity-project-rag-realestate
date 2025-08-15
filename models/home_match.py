# Main application module for HomeMatch

import os
import sys
from pathlib import Path

# Add project root to path to allow imports from other directories
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from models.listing_generator import ListingGenerator
from models.vector_db import VectorDBManager
from models.preference_manager import PreferenceManager
from models.listing_personalizer import ListingPersonalizer
from utils.helpers import setup_environment, create_directory_if_not_exists

class HomeMatch:
    """
    Main HomeMatch application class that coordinates all components.
    """
    
    def __init__(self):
        """
        Initialize the HomeMatch application.
        """
        # Check if environment is set up correctly
        if not setup_environment():
            print("Environment setup failed. Please check your API keys.")
            return
        
        # Create necessary directories
        create_directory_if_not_exists(os.path.join(project_root, "data"))
        create_directory_if_not_exists(os.path.join(project_root, "data", "vectordb"))
        
        # Initialize components
        self.listing_generator = ListingGenerator()
        self.vector_db = VectorDBManager(persist_directory=os.path.join(project_root, "data", "vectordb"))
        self.preference_manager = PreferenceManager()
        self.listing_personalizer = ListingPersonalizer()
        
        # Set file paths
        self.listings_file = os.path.join(project_root, "data", "listings.json")
    
    def generate_listings(self, num_listings=10, force_new=False):
        """
        Generate listings or load from file if they exist
        
        Args:
            num_listings (int): Number of listings to generate
            force_new (bool): Whether to force new listing generation
            
        Returns:
            list: List of generated listings
        """
        # Check if listings file exists
        if os.path.exists(self.listings_file) and not force_new:
            try:
                listings = self.listing_generator.load_listings_from_file(self.listings_file)
                return listings
            except:
                print("Error loading listings from file. Generating new listings...")
        
        # Generate new listings
        listings = self.listing_generator.generate_listings(num_listings)
        
        # Save listings to file
        self.listing_generator.save_listings_to_file(listings, self.listings_file)
        
        return listings
    
    def setup_vector_db(self, listings):
        """
        Set up the vector database with listings
        
        Args:
            listings (list): List of listings to store
        """
        self.vector_db.initialize_with_listings(listings)
    
    def collect_preferences(self, interactive=False):
        """
        Collect buyer preferences
        
        Args:
            interactive (bool): Whether to collect preferences interactively
            
        Returns:
            list: List of buyer preferences
            str: Combined preference query
        """
        # Collect preferences
        preferences = self.preference_manager.collect_preferences(interactive=interactive)
        
        # Display preferences
        self.preference_manager.display_preferences(
            self.preference_manager.default_questions, 
            preferences
        )
        
        # Combine preferences into query
        preference_query = self.preference_manager.combine_preferences(preferences)
        
        return preferences, preference_query
    
    def search_listings(self, preference_query, num_results=3):
        """
        Search for listings that match preferences
        
        Args:
            preference_query (str): Combined buyer preferences
            num_results (int): Number of results to return
            
        Returns:
            list: List of matching listings
        """
        return self.vector_db.search(preference_query, num_results)
    
    def personalize_listings(self, matching_listings, buyer_preferences):
        """
        Personalize listings based on buyer preferences
        
        Args:
            matching_listings (list): List of matching listings
            buyer_preferences (list): List of buyer preferences
            
        Returns:
            list: List of personalized listings
        """
        return self.listing_personalizer.personalize_listings(matching_listings, buyer_preferences)
    
    def run(self, num_listings=10, num_results=3, interactive=False, force_new_listings=False):
        """
        Run the complete HomeMatch application
        
        Args:
            num_listings (int): Number of listings to generate
            num_results (int): Number of results to return
            interactive (bool): Whether to collect preferences interactively
            force_new_listings (bool): Whether to force new listing generation
            
        Returns:
            list: List of personalized listings
        """
        print("=== RUNNING HOMEMATCH APPLICATION ===\n")
        
        # Step 1: Generate or load listings
        listings = self.generate_listings(num_listings, force_new_listings)
        
        # Step 2: Set up vector database
        self.setup_vector_db(listings)
        
        # Step 3: Collect buyer preferences
        buyer_preferences, preference_query = self.collect_preferences(interactive)
        
        # Step 4: Search for matching listings
        print("\nSearching for matching listings...")
        matching_listings = self.search_listings(preference_query, num_results)
        
        # Step 5: Personalize descriptions
        print("\nPersonalizing descriptions...")
        personalized_listings = self.personalize_listings(matching_listings, buyer_preferences)
        
        # Display results
        self.listing_personalizer.display_personalized_listings(personalized_listings)
        
        return personalized_listings
