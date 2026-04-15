# setup_database.py
# This script sets up the SQLite database for the application. It creates a `patients` table and populates it with sample data. Run this script before starting the FastAPI application to ensure the database is ready. 

# Purpose: This script initializes the SQLite database by creating the necessary table and inserting sample data. 
# It uses the built-in `sqlite3` library to manage the database connection and execute SQL commands. 
# The script first drops the `patients` table if it already exists to ensure a clean setup, then creates the table with the specified schema and inserts sample patient records. 
# Finally, it commits the changes and closes the connection.


import sqlite3

conn = sqlite3.connect("healthcare.db")
cursor = conn.cursor()

# used to delete old tables if exists
cursor.execute("DROP TABLE IF EXISTS patients")

# create patients table with columns for details
cursor.execute("""               
CREATE TABLE patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    gender TEXT,
    disease TEXT,
    doctor TEXT,
    admission_date TEXT
)
""")

# sample data to insert into patients table
data = [
    ("Amit Sharma", 45, "Male", "Diabetes", "Dr Sharma", "2024-01-10"),
    ("Neha Verma", 32, "Female", "Asthma", "Dr Gupta", "2024-02-15"),
    ("Rahul Singh", 60, "Male", "Heart Disease", "Dr Mehta", "2024-03-01"),
    ("Priya Patel", 28, "Female", "Flu", "Dr Sharma", "2024-03-20"),
    ("Ankit Jain", 50, "Male", "Diabetes", "Dr Gupta", "2024-04-05"),
    ("Sneha Kapoor", 40, "Female", "Hypertension", "Dr Mehta", "2024-04-18")
]

# bulk insert sample data into patients table using executemany for effieciency and accuracy to avaoid risk of sql injection.
cursor.executemany("""
INSERT INTO patients (name, age, gender, disease, doctor, admission_date)
VALUES (?, ?, ?, ?, ?, ?)
""", data)

conn.commit()
conn.close()

print("Database created")