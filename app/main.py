# main.py
# This is the main entry point for the FastAPI application. It defines the API endpoints and connects them to the appropriate services.
# Purpose: This module sets up the FastAPI application and defines the API routes. 
# The root endpoint ("/") returns a simple message to confirm that the API is running, while the "/query" endpoint 
# accepts POST requests with a natural language question, processes it using the `process_query` function from the `nl2sql_service`, 
# and returns the generated SQL query along with the results from the database.


from fastapi import FastAPI # FastAPI framework to build API
from app.services.nl2sql_service import process_query

# create FastAPI app instance
app = FastAPI()

# define root endpoint to check if API is running 
@app.get("/")
def home():
    return {"message": "NL2SQL API Running!!"}

# define /query endpoint to process user questions
@app.post("/query")
def query(data: dict): # takes json input with "question " key
    return process_query(data["question"])  # extracts question from input and sends to service for processing, returns response.
