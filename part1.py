import requests
import time
import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"SQLite Database created and connected to: {db_file}")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    
database = "prj-data.db"    
create_connection(database)


def fetch_data():
    url = 'https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(response.status_code)
        return None

def run_every_minute(duration_minutes):
    end_time = time.time() + duration_minutes * 60
    while time.time() < end_time:
        data = fetch_data()
        print(data)  # This would be replaced by a call to save data to a database
        time.sleep(60)  # Sleep for a minute

run_every_minute(60)


# sql_create_data_records_table = """
# CREATE TABLE IF NOT EXISTS data_records (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     factor TEXT,
#     pi REAL,
#     time TEXT
# );