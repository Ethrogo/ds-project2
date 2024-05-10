import requests
import time
import sqlite3
import sys
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"SQLite Database created and connected to: {db_file}")
        return conn
    except Error as e:
        print(e)
        sys.exit(1)
        
        
    
database = "prj-data.db"    
conn = create_connection(database)


def fetch_data():
    url = 'https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(response.status_code)
        return None

def insert_data(conn, data):
    sql = ''' INSERT INTO data_records(factor,pi,time)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()

def run_every_minute(duration_minutes):
    end_time = time.time() + duration_minutes * 60
    while time.time() < end_time:
        data = fetch_data()
        insert_data(conn, data)
        time.sleep(60)  

run_every_minute(60)


# sql_create_data_records_table = """
# CREATE TABLE IF NOT EXISTS data_records (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     factor TEXT,
#     pi REAL,
#     time TEXT
# );