# database.py
# This module provides a simple interface to connect to the SQLite database used in the application.
# Purpose: This model handles the database connection and allows us to execute SQL queries against the `healthcare.db` SQLite database. 
# It uses the built-in `sqlite3` library to manage the connection and execute queries. 
# The `get_connection` function establishes a connection to the database and sets the row factory to allow for dict-like access to query results.


import sqlite3  # built-in python library for SQLite

# function to create db connection and set row factory for dict-like access to results 
def get_connection():
    conn = sqlite3.connect("healthcare.db") # connects to local SQLite db 
    conn.row_factory = sqlite3.Row # allows us to access columns by name instead of index 
    return conn # returns connection