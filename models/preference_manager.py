# Preference Manager Module
# Responsible for collecting and processing buyer preferences

class PreferenceManager:
    """
    Class for managing buyer preferences.
    """
    
    def __init__(self):
        """
        Initialize the PreferenceManager.
        """
        # Default questions for collecting preferences
        self.default_questions = [
            "How big do you want your house to be?",
            "What are 3 most important things for you in choosing this property?",
            "Which amenities would you like?",
            "Which transportation options are important to you?",
            "How urban do you want your neighborhood to be?"
        ]
        
        # Default answers for testing
        self.default_answers = [
            "A comfortable three-bedroom house with a spacious kitchen and a cozy living room.",
            "A quiet neighborhood, good local schools, and convenient shopping options.",
            "A backyard for gardening, a two-car garage, and a modern, energy-efficient heating system.",
            "Easy access to a reliable bus line, proximity to a major highway, and bike-friendly roads.",
            "A balance between suburban tranquility and access to urban amenities like restaurants and theaters."
        ]
    
    def collect_preferences(self, questions=None, interactive=False, default_answers=None):
        """
        Collect buyer preferences either interactively or using default answers
        
        Args:
            questions (list): List of questions to ask (defaults to self.default_questions)
            interactive (bool): Whether to collect answers interactively
            default_answers (list): Default answers to use if not interactive
            
        Returns:
            list: List of buyer preferences
        """
        # Use default questions if none provided
        if questions is None:
            questions = self.default_questions
        
        # Use default answers if none provided
        if default_answers is None:
            default_answers = self.default_answers
        
        answers = []
        
        if interactive:
            print("Please answer the following questions about your home preferences:")
            for i, question in enumerate(questions):
                print(f"\n{i+1}. {question}")
                answer = input("Your answer: ")
                answers.append(answer)
        else:
            # Use default answers for testing
            answers = default_answers
            
        return answers
    
    def combine_preferences(self, preferences):
        """
        Combine multiple preference answers into a single query string
        
        Args:
            preferences (list): List of preference answers
            
        Returns:
            str: Combined preference query
        """
        return " ".join(preferences)
    
    def display_preferences(self, questions, preferences):
        """
        Display the questions and corresponding preferences
        
        Args:
            questions (list): List of questions
            preferences (list): List of preference answers
        """
        print("Buyer Preferences:")
        for i, (question, answer) in enumerate(zip(questions, preferences)):
            print(f"{i+1}. {question}")
            print(f"   {answer}")
        print()  # Add empty line at end
