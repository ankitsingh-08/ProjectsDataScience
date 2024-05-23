import requests
import pandas as pd

API_T1 = 'https://api.binance.com/api/v3/ticker/24hr'

result = requests.get(API_T1)

if result.status_code == 200:
    data = result.json()
    df = pd.DataFrame(data)
    df.to_csv("task1.csv")
    print("CSV dataset created")
else:
    print("Failed")
