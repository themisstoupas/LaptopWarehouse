import psycopg2
from psycopg2 import sql
from psycopg2.extras import RealDictCursor


class DatabaseConnection:

    def execute_query(self, query: str, params: tuple):
        try:
            with psycopg2.connect(
                    dbname="postgres",
                    user="postgres",
                    password="postgres",
                    host="localhost",
                    port="5432"
            ) as conn:
                with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                    cursor.execute(query, params)
                    return cursor.fetchone()
        except Exception as e:
            print(f"An unexpected error occurred while executing query: {e}")
            return None

    def fetch_data(self, query: str):
        try:
            with psycopg2.connect(
                    dbname="postgres",
                    user="postgres",
                    password="postgres",
                    host="localhost",
                    port="5432"
            ) as conn:
                with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                    cursor.execute(query)
                    return cursor.fetchall()
        except Exception as e:
            print(f"An unexpected error occurred while fetching data: {e}")
            return []
