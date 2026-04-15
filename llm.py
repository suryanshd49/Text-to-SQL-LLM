import requests

def convert_to_sql(text):

    schema = """
Tables:

employees(id, name, dept_id, salary)

departments(dept_id, dept_name, location)

Relationships:
employees.dept_id = departments.dept_id
"""

    prompt = f"""
You are a SQL expert.

Convert natural language to SQL query.

Database Schema:
{schema}

Rules:
- Return only SQL
- No explanation
- No markdown

Question:
{text}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    sql = response.json()["response"]

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    return sql