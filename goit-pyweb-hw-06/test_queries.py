import sqlite3

def execute_queries():
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()

    for i in range(1, 11):
        with open(f'query_{i}.sql', 'r') as file:
            sql_query = file.read()

        cursor.execute(sql_query)

        print(f"Results for Query {i}:")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        print() 

    conn.close()

execute_queries()
