from app.vanna_client import generate_sql, run_sql

def process_query(question: str):
    try:
        sql = generate_sql(question)
        result = run_sql(sql)

        return {
            "sql": sql,
            "result": result
        }

    except Exception as e:
        return {
            "error": str(e)
        }