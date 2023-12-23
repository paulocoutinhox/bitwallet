import os

import requests


def get_bitcoin_value_in_usd():
    response = requests.get(
        "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    )
    data = response.json()
    return data["bitcoin"]["usd"]


def get_bitcoin_value_in_brl():
    response = requests.get(
        "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl"
    )
    data = response.json()
    return data["bitcoin"]["brl"]


def get_wallet_balance(wallet_address):
    url = f"https://blockchain.info/balance?active={wallet_address}"
    response = requests.get(url)
    data = response.json()
    balance_satoshis = data[wallet_address]["final_balance"]
    # convert from satoshis to Bitcoin
    balance_bitcoins = balance_satoshis / 1e8
    return balance_bitcoins


wallet_address = os.getenv("BTC_WALLET")

balance = get_wallet_balance(wallet_address)
bitcoin_value_in_usd = get_bitcoin_value_in_usd()
bitcoin_value_in_brl = get_bitcoin_value_in_brl()

balance_in_usd = balance * bitcoin_value_in_usd
balance_in_brl = balance * bitcoin_value_in_brl

print(
    f"You have {balance} BTC, which is equivalent to ${balance_in_usd:.2f} USD or R$ {balance_in_brl:.2f} BRL"
)
