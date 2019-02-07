## Interface for trading with tradasatoshi


### Examples


```
# Get all balances
get_private_data(
    uri = "https://tradesatoshi.com/api/private/getbalances"
)
```


```
# Get order info
get_private_data(
    uri = "https://tradesatoshi.com/api/private/getorder",
    OrderId=123,
)
```


```
# Get all orders info
get_private_data(
    uri = "https://tradesatoshi.com/api/private/getorders",
    # Market='LTC_BTC', 
    # count = 20
)
```


```
# Place an order
get_private_data(
    uri = "https://tradesatoshi.com/api/private/submitorder",
    Market='LTC_BTC', 
    Type = 'buy',
    Amount=1,
    Price=0.1
)
```


```
# Cancel an order
get_private_data(
    uri = "https://tradesatoshi.com/api/private/cancelorder",
    Type='Single', 
    OrderId=123
)
```


```
# Get trade history
get_private_data(
    uri = "https://tradesatoshi.com/api/private/gettradehistory",
    #Market='LTC_BTC', 
    count=20,
    #PageNumber=0
)
```


```
# Deposits history
get_private_data(
    uri = "https://tradesatoshi.com/api/private/getdeposits",
    Currency='DOGE',
    Count=20
)
```
