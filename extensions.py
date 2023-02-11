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
    def get_price(base: str, quote: str, amount: str):
        """

        :param base: Имя валюты, цену в которой надо узнать
        :param quote: Имя валюты, цену на которую надо узнать
        :param amount: количество переводимой валюты
        :return: возвращает нужную сумму в валюте
        """

        try:
            base_ticker = currency[base]
        except KeyError:
            raise APIException(f'Не удалось найти валюту {base}.')

        try:
            quote_ticker = currency[quote]
        except KeyError:
            raise APIException(f'Не удалось найти валюту "{quote}".')

        if base == quote:
            raise APIException(f'Невозможно перевести одинаковые валюты "{quote}".')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество "{amount}"')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        total_base = json.loads(r.content)[currency[quote]]
        total_base = round(amount * total_base, 2)
        return total_base
