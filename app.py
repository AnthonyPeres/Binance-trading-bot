from binance.spot import Spot
from json import load
import os
from dotenv import load_dotenv
load_dotenv()


BINANCE_API_KEY = os.getenv('BINANCE_API_KEY')
BINANCE_SECRET_KEY = os.getenv('BINANCE_SECRET_KEY')

client = Spot()
print(client.time())

client = Spot(key=BINANCE_API_KEY, secret=BINANCE_SECRET_KEY)
print(client.account())
