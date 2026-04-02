# NL2SQL System using FastAPI + Gemini

## Overview
This project converts natural language queries into SQL and executes them on a SQLite database.

## Tech Stack
- FastAPI (Backend)
- Streamlit (Frontend)
- Google Gemini (LLM)
- SQLite (Database)

## Setup

1. Create virtual env
2. Install dependencies:
   pip install -r requirements.txt

3. Set API Key:
   setx GEMINI_API_KEY "your_key"

4. Setup DB:
   python scripts/setup_database.py

5. Run Backend:
   uvicorn app.main:app --reload

6. Run UI:
   streamlit run ui.py

## Sample Queries
- Show all patients
- List patients with diabetes
- Count total patients
- Show female patients

## Features
- Natural language to SQL
- Real-time query execution
- Interactive UI