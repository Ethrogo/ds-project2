import requests
import time

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
print("something")