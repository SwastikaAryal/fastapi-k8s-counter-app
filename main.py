from fastapi import FastAPI
import sqlite3

app = FastAPI()
conn = sqlite3.connect("requests.db", check_same_thread=False)
cursor = conn.cursor()

# Create table to store request count
cursor.execute("CREATE TABLE IF NOT EXISTS request_count (count INTEGER)")
cursor.execute("INSERT INTO request_count (count) VALUES (0)")
conn.commit()

@app.get("/count")
def read_count():
    cursor.execute("SELECT count FROM request_count")
    count = cursor.fetchone()[0]
    cursor.execute("UPDATE request_count SET count = count + 1")
    conn.commit()
    return {"count": count}
