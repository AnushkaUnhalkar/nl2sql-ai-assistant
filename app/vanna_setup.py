from vanna.chromadb import ChromaDB_VectorStore
from vanna.openai import OpenAI_Chat
import os

# Create Vanna class
class MyVanna(ChromaDB_VectorStore, OpenAI_Chat):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        OpenAI_Chat.__init__(self, config=config)

# Initialize Vanna
vn = MyVanna(config={
    "api_key": os.getenv("OPENAI_API_KEY"),
    "model": "gpt-3.5-turbo",   # or gpt-4 if available
    "persist_directory": "vanna_db"   # IMPORTANT
})

# Connect to SQLite
vn.connect_to_sqlite("healthcare.db")

# Train schema
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