# Vector Database Module
# Responsible for managing the vector database operations

import os
from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.schema import Document

class VectorDBManager:
    """
    Class for managing vector database operations.
    """
    
    def __init__(self, persist_directory="data/vectordb"):
        """
        Initialize the VectorDBManager.
        
        Args:
            persist_directory (str): Directory to persist the vector database
        """
        self.persist_directory = persist_directory
        self.embeddings = OpenAIEmbeddings(
            openai_api_key=os.environ.get("OPENAI_API_KEY"),
            openai_api_base=os.environ.get("OPENAI_API_BASE", "https://openai.vocareum.com/v1")
        )
        
        # Create directory if it doesn't exist
        os.makedirs(persist_directory, exist_ok=True)
        
        # Try to load existing database or create a new one
        try:
            self.vectordb = Chroma(
                persist_directory=persist_directory,
                embedding_function=self.embeddings
            )
            print(f"Loaded existing vector database from {persist_directory}")
        except:
            print(f"No existing database found at {persist_directory}. Will create a new one when data is added.")
            self.vectordb = None
    
    def prepare_documents_for_embedding(self, listings):
        """
        Convert listing dictionaries to Document objects for embedding
        
        Args:
            listings (list): List of listing dictionaries
            
        Returns:
            list: List of Document objects
        """
        documents = []
        for i, listing in enumerate(listings):
            # Create a combined text representation of the listing
            text = f"""
            Neighborhood: {listing['neighborhood']}
            Price: {listing['price']}
            Bedrooms: {listing['bedrooms']}
            Bathrooms: {listing['bathrooms']}
            House Size: {listing['house_size']}
            
            Description: {listing['description']}
            
            Neighborhood Description: {listing['neighborhood_description']}
            """
            
            # Create Document object with metadata
            doc = Document(
                page_content=text,
                metadata={
                    'id': i,
                    'neighborhood': listing['neighborhood'],
                    'price': listing['price'],
                    'bedrooms': listing['bedrooms'],
                    'bathrooms': listing['bathrooms'],
                    'house_size': listing['house_size'],
                    'description': listing['description'],
                    'neighborhood_description': listing['neighborhood_description']
                }
            )
            documents.append(doc)
        
        return documents
    
    def initialize_with_listings(self, listings):
        """
        Initialize or update vector database with listings
        
        Args:
            listings (list): List of listing dictionaries
        """
        # Prepare documents for embedding
        documents = self.prepare_documents_for_embedding(listings)
        
        # Initialize ChromaDB and add documents
        self.vectordb = Chroma.from_documents(
            documents=documents,
            embedding=self.embeddings,
            persist_directory=self.persist_directory
        )
        
        # Persist the database
        self.vectordb.persist()
        
        print(f"Vector database initialized with {len(listings)} listings")
    
    def search(self, query, num_results=3):
        """
        Search for listings that match a query
        
        Args:
            query (str): The search query
            num_results (int): Number of results to return
            
        Returns:
            list: List of matching listings with similarity scores
        """
        if not self.vectordb:
            raise ValueError("Vector database not initialized. Call initialize_with_listings first.")
        
        # Perform similarity search
        results = self.vectordb.similarity_search_with_score(
            query,
            k=num_results
        )
        
        # Extract listings and scores
        matches = []
        for doc, score in results:
            # Convert score to similarity (ChromaDB returns distance, lower is better)
            similarity = 1 - score
            
            # Get listing details from document metadata
            listing = {
                'neighborhood': doc.metadata['neighborhood'],
                'price': doc.metadata['price'],
                'bedrooms': doc.metadata['bedrooms'],
                'bathrooms': doc.metadata['bathrooms'],
                'house_size': doc.metadata['house_size'],
                'description': doc.metadata['description'],
                'neighborhood_description': doc.metadata['neighborhood_description'],
                'similarity_score': similarity
            }
            
            matches.append(listing)
        
        return matches
