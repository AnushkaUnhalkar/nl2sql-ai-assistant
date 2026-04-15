# validator.py
# This module contains functions to validate SQL queries before execution.
# Purpose: This module ensures that only safe and valid SQL queries are executed against the database, 
# preventing potential SQL injection attacks and maintaining the integrity of the database.

# Function to validate SQL query to ensure it is a safe SELECT statement without any dangerous keywords like DROP, DELETE, UPDATE, INSERT, or ALTER. 
# This is crucial to prevent SQL injection attacks and ensure the security of the database.

def validate_sql(sql: str):
    sql = sql.strip().lower()

    # Only allow SELECT queries to prevent any modifications to the database and ensure read-only access for the application.
    if not sql.startswith("select"):
        raise ValueError("Only SELECT queries are allowed")
    
    dangerous = ["drop", "delete", "update", "insert", "alter"]

    for word in dangerous:
        if word in sql:
            raise ValueError(f"Query contains dangerous keyword: {word}")

    return sql