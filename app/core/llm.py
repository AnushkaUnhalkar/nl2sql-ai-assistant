# llm.py
# This module contains functions to interact with the Gemini LLM for SQL generation and result summarization.
# Purpose: This module abstracts the LLM interactions, making it easier to maintain and update the AI logic separately from the main application flow.

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variable from .env file
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Ensure API key is available
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

genai.configure(api_key=api_key)


# Function to generate SQL query from natural language question using Gemini LLM 
def generate_sql(question: str):
    prompt = f"""
You are an expert SQL generator.

Database: SQLite

Table: patients
Columns:
- id
- name
- age
- gender
- disease
- doctor
- admission_date

Return ONLY SQL query.

Question: {question}

SQL:
"""

    model = genai.GenerativeModel("gemini-1.5-flash") # Use the latest Gemini model for better performance
    response = model.generate_content(prompt) # Generate SQL query based on the prompt

    sql = response.text.strip() # Extract the generated SQL query from response

    if "```" in sql:
        sql = sql.split("```")[1]

    return sql


# Function to summarize SQL query results in simple English using Gemini LLM
def summarize_result(question: str, result: list):
    prompt = f"""
User Question: {question}

SQL Result:
{result}

Explain the result in simple English.
"""

    model = genai.GenerativeModel("gemini-1.5-flash") 
    response = model.generate_content(prompt) # Generate summary based on the prompt

    return response.text.strip() # Extract the summary text from response and return it