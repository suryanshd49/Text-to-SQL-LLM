import mysql.connector

def run_sql(query):

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="company"
    )

    cursor = conn.cursor()

    cursor.execute(query)

    result = cursor.fetchall()

    conn.close()

    return result