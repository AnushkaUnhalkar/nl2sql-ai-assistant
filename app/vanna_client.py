import os
import sqlite3
from dotenv import load_dotenv
from google import genai

# Load env
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("❌ GOOGLE_API_KEY not found in .env file")

# Create client
client = genai.Client(api_key=api_key)


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

    response = client.models.generate_content(
        model="gemini-2.0-flash",   # ✅ UPDATED MODEL
        contents=prompt
    )

    sql = response.text.strip()

    if "```" in sql:
        sql = sql.split("```")[1]

    return sql


def run_sql(sql: str):
    conn = sqlite3.connect("healthcare.db")
    cursor = conn.cursor()

    cursor.execute(sql)
    rows = cursor.fetchall()

    columns = [desc[0] for desc in cursor.description]

    conn.close()

    return [dict(zip(columns, row)) for row in rows]