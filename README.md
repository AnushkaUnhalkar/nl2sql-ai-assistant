# 🧠 NL2SQL AI Assistant

Convert natural language questions into SQL queries and visualize results instantly using AI.

---

## 🚀 Overview

The **NL2SQL AI Assistant** allows users to ask questions in plain English and automatically converts them into SQL queries using an LLM (Gemini). The results are fetched from a SQLite database and displayed in a clean UI with optional visualizations.

---

## ✨ Features

* 💬 Ask questions in natural language
* 🧠 AI-generated SQL queries (NL → SQL)
* 📊 Automatic data visualization
* ⚡ FastAPI backend for query processing
* 🎨 Streamlit frontend with chat UI
* 🗄️ SQLite database integration

---

## 🏗️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** FastAPI
* **Database:** SQLite
* **AI Model:** Gemini API
* **Language:** Python

---

## 📂 Project Structure

```
nl2sql-project/
│
├── app/
│   ├── core/                     # 🔥 Core logic layer (modular)
│   │   ├── llm.py               # Gemini (SQL generation + summary)
│   │   ├── db.py                # SQLite execution
│   │   ├── validator.py        # SQL safety validation
│   │   ├── chart.py            # Chart generation (base64)
│   │   └── vanna_agent.py      # (Optional) Vanna integration
│   │
│   ├── services/
│   │   └── nl2sql_service.py   # Orchestration layer (pipeline)
│   │
│   ├── main.py                 # FastAPI entry point
│   ├── database.py             # (Optional – legacy, can remove later)
│   ├── setup_database.py       # DB initialization script
│   ├── vanna_setup.py          # Vanna training setup
│
├── ui.py                       # Streamlit frontend
│
├── healthcare.db               # SQLite database
├── .env                        # API keys (NOT pushed)
├── .gitignore                  # Ignore venv, pycache, etc.
├── requirements.txt            # Dependencies
├── README.md                   # Project documentation
│
└── venv/                       # Virtual environment (ignored)

```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/AnushkaUnhalkar/nl2sql-ai-assistant.git
cd nl2sql-ai-assistant
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup environment variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

### 5️⃣ Run backend (FastAPI)

```bash
uvicorn app.main:app --reload
```

Backend runs on:
👉 http://127.0.0.1:8000

---

### 6️⃣ Run frontend (Streamlit)

```bash
streamlit run ui.py
```

---

## 💡 Example Queries

* Show all patients
* List patients with diabetes
* Count total number of patients
* Show patients admitted after 2023

---

## 📊 How It Works

1. User enters a question
2. Gemini converts it into SQL
3. SQL query runs on SQLite DB
4. Results are returned via FastAPI
5. Streamlit displays data + charts

---

## 🔒 Security Notes

* API keys are stored in `.env` (not pushed to GitHub)
* `.env.example` is provided for reference

---

## 🚀 Future Improvements

* ✅ Support multiple tables
* 🔐 Add authentication
* ☁️ Deploy on cloud (Render / Streamlit Cloud)
* 📈 Advanced visualizations

---

## 👩‍💻 Author

**Anushka Unhalkar**

---
