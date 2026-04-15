# vanna_agent.py
# This module defines the MyVanna class which integrates ChromaDB for vector storage and OpenAI for chat capabilities.
# Purpose: This class serves as the core agent that interacts with both the vector database and the OpenAI API, 
# allowing for seamless integration of AI functionalities in the application.


from vanna.chromadb import ChromaDB_VectorStore
from vanna.openai import OpenAI_Chat
import os

# MyVanna class that combines ChromaDB_VectorStore and OpenAI_Chat functionalities to create a powerful agent for handling AI interactions in the application.
class MyVanna(ChromaDB_VectorStore, OpenAI_Chat):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config) # Initialize ChromaDB_VectorStore with provided config 
        OpenAI_Chat.__init__(self, config=config) # Initialize OpenAI_Chat with provided config


# Initialize Vanna agent with necessary configuration for both ChromaDB and OpenAI
vn = MyVanna(config={
    "api_key": os.getenv("OPENAI_API_KEY"),
    "model": "gpt-3.5-turbo",
    "persist_directory": "vanna_db"
})

# Connect DB to SQLite database containing healthcare data for training and querying the model with relevant info
vn.connect_to_sqlite("healthcare.db")

# Train schema to help Vanna understand the structure of db
vn.train(
    ddl="""
    CREATE TABLE patients (
        id INTEGER,
        name TEXT,
        age INTEGER,
        gender TEXT,
        disease TEXT,
        doctor TEXT,
        admission_date TEXT
    );
    """
)