# db.py
# This module contains functions to interact with the SQLite database, including executing SQL queries and retrieving results.
# Purpose: This module abstracts the database interactions, allowing for easier maintenance and separation of concerns in the application. 
# It also includes validation to ensure that only safe SQL queries are executed against the database.


from app.database import get_connection
from app.core.validator import validate_sql

# Function to execute a validated SQL query against the SQLite db and returns results.
def run_sql(sql: str):
    sql = validate_sql(sql)
    
    # Get a connection to SQLite db and execute query
    conn = get_connection()
    cursor = conn.cursor()

    # Execute the validated SQL query and fetch results
    cursor.execute(sql)
    rows = cursor.fetchall()

    # Get column names from cursor description to create a list of dictionaries for better readability of results
    columns = [desc[0] for desc in cursor.description]

    conn.close()

    return [dict(zip(columns, row)) for row in rows]