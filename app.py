from binance import Client
from json import load
import os
from dotenv import load_dotenv
load_dotenv()


BINANCE_API_KEY = os.getenv('BINANCE_API_KEY')
BINANCE_SECRET_KEY = os.getenv('BINANCE_SECRET_KEY')


client = Client(BINANCE_API_KEY, BINANCE_SECRET_KEY)
print("Connected to binance")

print(client.get_account())
