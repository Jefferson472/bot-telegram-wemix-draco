import os
import requests
from dotenv import load_dotenv
from crypto_price import Crypto_Price


load_dotenv('.env')
TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
CHAT_ID = os.environ['CHAT_ID']

crypto_price = Crypto_Price()
text_cotent = (
    crypto_price.get_draco_wemix_price(),
    crypto_price.get_hidra_wemix_price()
)

METHOD_NAME = 'sendMessage'
url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/{METHOD_NAME}?chat_id={CHAT_ID}&text={text_cotent}'

requests.post(url)

print(url)
