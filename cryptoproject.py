import requests

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": "6",
    "page": "1",
    "sparkline": False
}
class Crypto(object):
    def __init__(self, name, symbol, value, marketcap, dailymove, dailyvolume):
        self.name = name
        self.symbol = symbol.upper()
        self.value = value
        self.marketcap = marketcap
        self.dailymove = dailymove
        self.dailyvolume = dailyvolume
    
    def __str__(self):
        return f"{self.name} {self.symbol} \n Cena: {self.value} USD\n Market cap: {self.marketcap} USD\n Dnevni premik: {self.dailymove}%\n Dnevni volumen: {self.dailyvolume} USD"

response = requests.get(url, params=params)
data = response.json()

coins= []

for coin_data in data:
    symbol = coin_data["symbol"]
    if "usd" in symbol.lower():
        continue
    name = coin_data["name"]
    value = coin_data["current_price"]
    marketcap = coin_data["market_cap"]
    dailymove = coin_data["price_change_percentage_24h"]
    dailyvolume = coin_data["total_volume"]

    coin = Crypto(name, symbol, value, marketcap, dailymove, dailyvolume)
    coins.append(coin)

#for coin in coins:
    #print(coin)

def Izberi_kovanec(coins):
    izberi = input("Izberi kovanec(ticker ali ime): ").lower().strip()

    if izberi == "exit":
        return "exit"

    for coin in coins:
        if coin.name.lower() == izberi or coin.symbol.lower() == izberi:
            print(coin)
            return coin
        
    print("Kovanec ni najden. Poskusi znova.")
    return None

coin = None

while coin is None:
    coin = Izberi_kovanec(coins)


    

