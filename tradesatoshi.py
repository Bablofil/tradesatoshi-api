import requests
import hmac, hashlib
import time
import urllib
import base64
import json


API_KEY = ''
API_SECRET = ''

def get_private_data(uri, **kwargs):
    nonce = int(time.time()*1000)

    q = json.dumps(kwargs, separators=(',', ':'))
    b64_q = base64.b64encode(bytes(q, 'utf-8'))
    raw_s = API_KEY + "POST" + urllib.parse.quote_plus(uri).lower() + str(nonce) + b64_q.decode('utf-8')

    hmacsignature = base64.b64encode(hmac.new(base64.b64decode(API_SECRET), raw_s.encode('utf-8'), hashlib.sha512).digest())

    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'User-Agent': 'Mozilla/4.0 (compatible; TradeSatoshi API Python client; )',
        'Authorization': 'Basic ' + API_KEY + ':'+hmacsignature.decode('utf-8')+':'+str(nonce)
    }

    r = requests.post(uri, data=q, headers=headers, verify=False)

    try:
        print(r.json())
    except:
        print(r.text)


# Баланс по монете
get_private_data(
    uri = "https://tradesatoshi.com/api/private/getbalance",
    Currency='DOGE',
)

# Баланс по всем монетам
#get_private_data(
#    uri = "https://tradesatoshi.com/api/private/getbalances"
#)

# Информация по ордеру
#get_private_data(
#    uri = "https://tradesatoshi.com/api/private/getorder",
#    OrderId=123,
#)

# Получить информацию по ордерам
#get_private_data(
#    uri = "https://tradesatoshi.com/api/private/getorders",
#    # Market='LTC_BTC', 
#    # count = 20
#)

# Разместить ордер
#get_private_data(
#    uri = "https://tradesatoshi.com/api/private/submitorder",
#    Market='LTC_BTC', 
#    Type = 'buy',
#    Amount=1,
#    Price=0.1
#)

# Отменить ордер
#get_private_data(
#    uri = "https://tradesatoshi.com/api/private/cancelorder",
#    Type='Single', 
#    OrderId=123
#)

# Получить историю торгов
#get_private_data(
#    uri = "https://tradesatoshi.com/api/private/gettradehistory",
#    #Market='LTC_BTC', 
#    count=20,
#    #PageNumber=0
#)

# История пополнений
#get_private_data(
#    uri = "https://tradesatoshi.com/api/private/getdeposits",
#    Currency='DOGE',
#    Count=20
#)

