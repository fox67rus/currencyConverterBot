import json

import requests

currency = {
    'рубль': 'RUB',
    'доллар': 'USD',
    'евро': 'EUR'
}


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        try:
            quote_ticker = currency[quote]
        except KeyError:
            raise APIException(f'Не удалось найти валюту {quote}.')

        try:
            base_ticker = currency[base]
        except KeyError:
            raise APIException(f'Не удалось найти валюту {base}.')

        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[currency[base]]

        return total_base
