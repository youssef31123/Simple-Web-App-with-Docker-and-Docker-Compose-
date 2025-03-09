from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# Database connection details from environment variables
DB_NAME = os.getenv("POSTGRES_DB", "mydb")
DB_USER = os.getenv("POSTGRES_USER", "user")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = os.getenv("DB_PORT", "5432")

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
        )
        return conn
    except Exception as e:
        return str(e)

@app.route("/")
def home():
    conn = connect_db()
    if isinstance(conn, str):  # If connection fails, return error message
        return f"Database connection failed: {conn}"
    return "Connected to PostgreSQL successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
