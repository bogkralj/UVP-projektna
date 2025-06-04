import requests

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": "5",
    "page": "1",
    "sparkline": False
}


response = requests.get(url, params=params)
data = response.json()

for coin in data:
    print(f"{coin['name']} ({coin['symbol']}): Market cap = {coin['market_cap']}")

