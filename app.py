from llm import convert_to_sql
from db import run_sql

while True:

    text = input("Ask question: ")

    sql = convert_to_sql(text)

    print("Generated SQL:", sql)

    result = run_sql(sql)

    print("Result:", result)