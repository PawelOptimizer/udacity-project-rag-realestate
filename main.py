#!/usr/bin/env python3
# Main script to run the HomeMatch application

import os
import sys
from pathlib import Path

# Add project root to path to allow imports from other directories
project_root = Path(__file__).parent
sys.path.append(str(project_root))

from models.home_match import HomeMatch

def main():
    """
    Run the HomeMatch application
    """
    # Initialize HomeMatch
    app = HomeMatch()
    
    # Run the application with default settings
    print("Running HomeMatch with default preferences...")
    app.run(num_listings=10, num_results=3, interactive=False)
    
    # Optionally, run with different preferences
    run_alternative = input("\nWould you like to run HomeMatch with alternative preferences? (y/n): ")
    if run_alternative.lower() == 'y':
        alternative_preferences = [
            "I'm looking for a luxury condo with at least 2 bedrooms in an urban setting.",
            "Modern design, high-end finishes, and good security are my priorities.",
            "I'd like a fitness center, rooftop terrace, and concierge service if possible.",
            "I need to be within walking distance of public transit and close to downtown.",
            "I prefer a vibrant urban neighborhood with restaurants, shopping, and nightlife."
        ]
        
        # Override default preferences in PreferenceManager
        app.preference_manager.default_answers = alternative_preferences
        
        # Run with alternative preferences
        print("\nRunning HomeMatch with alternative preferences...")
        app.run(num_results=3, interactive=False)
    
    print("\nHomeMatch application completed successfully!")

if __name__ == "__main__":
    main()
