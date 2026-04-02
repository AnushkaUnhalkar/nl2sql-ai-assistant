import sqlite3

conn = sqlite3.connect("healthcare.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS patients")

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

data = [
    ("Amit Sharma", 45, "Male", "Diabetes", "Dr Sharma", "2024-01-10"),
    ("Neha Verma", 32, "Female", "Asthma", "Dr Gupta", "2024-02-15"),
    ("Rahul Singh", 60, "Male", "Heart Disease", "Dr Mehta", "2024-03-01"),
    ("Priya Patel", 28, "Female", "Flu", "Dr Sharma", "2024-03-20"),
    ("Ankit Jain", 50, "Male", "Diabetes", "Dr Gupta", "2024-04-05"),
    ("Sneha Kapoor", 40, "Female", "Hypertension", "Dr Mehta", "2024-04-18")
]

cursor.executemany("""
INSERT INTO patients (name, age, gender, disease, doctor, admission_date)
VALUES (?, ?, ?, ?, ?, ?)
""", data)

conn.commit()
conn.close()

print("✅ Database created")