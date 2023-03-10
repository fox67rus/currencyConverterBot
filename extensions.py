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
         Конвертирует валюту base в quote с указанным количеством amount
        :param base: что конвертируем
        :param quote: во что конвертируем
        :param amount: количество переводимой валюты
        :return: возвращает нужную сумму в валюте
        """

        try:
            base_ticker = currency[base]
        except KeyError:
            raise APIException(f'Не удалось найти валюту "{base}".'
                               f'\n\nВведите /values, для получения списка доступных валют.')

        try:
            quote_ticker = currency[quote]
        except KeyError:
            raise APIException(f'Не удалось найти валюту "{quote}".'
                               f'\n\nВведите /values, для получения списка доступных валют.')

        if base == quote:
            raise APIException(f'Невозможно перевести одинаковые валюты "{quote}".')

        try:
            amount = float(amount)

        except ValueError:
            raise APIException(f'Не удалось обработать количество "{amount}". '
                               f'Введите корректное положительное числовое значение')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        total_base = json.loads(r.content)[currency[quote]]
        total_base = round(amount * total_base, 3)
        return total_base
