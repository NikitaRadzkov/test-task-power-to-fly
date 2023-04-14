import logging
import requests
from datetime import timedelta
from currency_client.cache import Cache


class CurrencyClient:
    def __init__(self, **kwargs):
        self.cache = kwargs.pop('cache', Cache)
        self.cache_duration = kwargs.pop('minutes', 0) * 60 + kwargs.pop('seconds', 0)
        self.cache = self.cache(timedelta(seconds=self.cache_duration))
        self.logger = logging.getLogger(__name__)

    def get_currency(self, currency_code):
        cached_value = self.cache.get(currency_code)
        if cached_value is not None:
            self.logger.info(f'Get cached data of {currency_code} - {cached_value}')
            return cached_value
        else:
            url = f'https://api.exchangeratesapi.io/latest?base={currency_code}'
            self.logger.info(f'{url} - GET')
            response = requests.get(url)
            self.logger.info(f'{url} - {response.status_code} - {response.text[:50]}...')
            response.raise_for_status()
            data = response.json()
            print(data)
            rate = data['rates']['EUR']
            self.cache.set(currency_code, rate)
            return rate

    def set_interval(self, **kwargs):
        self.cache.clear()
        self.cache_duration = kwargs.pop('minutes', 0) * 60 + kwargs.pop('seconds', 0)
        self.cache = self.cache(timedelta(seconds=self.cache_duration))

    def clear_cache(self):
        self.cache.clear()
