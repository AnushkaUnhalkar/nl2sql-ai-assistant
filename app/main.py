from fastapi import FastAPI
from app.services.nl2sql_service import process_query

app = FastAPI()

@app.get("/")
def home():
    return {"message": "NL2SQL API Running 🚀"}

@app.post("/query")
def query(data: dict):
    return process_query(data["question"])