# nl2sql_service.py
# This service handles the processing of natural language queries and their conversion to SQL.
# Purpose: This module acts as the bridge between the AI model and Database. 

# used to convert question to sql and run it against db and return results
# nl2sql_service.py
# This service handles the processing of natural language queries and their conversion to SQL.
# Purpose: This module acts as the bridge between the AI model and Database. 

# used to convert question to sql and run it against db and return results
from app.core.vanna_agent import vn
from app.core.llm import summarize_result
from app.core.db import run_sql
from app.core.chart import generate_chart

# main function to process user query
def process_query(question: str):
    # error handling block to catch any issues with SQL generation or execution 
    try: 
        sql = vn.generate_sql(question) # send question to Gemini to get sql query
        
        result = run_sql(sql) # execute sql on db and get results
        
        summary = summarize_result(question, result) # summarize results for better user understanding 
        
        chart = generate_chart(result) # generate chart if numeric data exists in results

        # return both generated sql and query results to the API response
        return {
            "sql": sql,
            "result": result,   
            "summary": summary,
            "chart": chart
        }

    # catch any exceptions and return error msg in response
    except Exception as e:
        return {
            "error": str(e)
        } 

# summarize_result
from app.core.db import run_sql
from app.core.chart import generate_chart

# main function to process user query
def process_query(question: str):
    # error handling block to catch any issues with SQL generation or execution 
    try: 
        sql = vn.generate_sql(question) # send question to Gemini to get sql query 
        
        result = run_sql(sql) # execute sql on db and get results
        
        summary = summarize_result(question, result) # summarize results for better user understanding 
        
        chart = generate_chart(result) # generate chart if numeric data exists in results

        # return both generated sql and query results to the API response
        return {
            "sql": sql,
            "result": result,   
            "summary": summary,
            "chart": chart
        }

    # catch any exceptions and return error msg in response
    except Exception as e:
        return {
            "error": str(e)
        }