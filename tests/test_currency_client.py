import time
from currency_client.client import CurrencyClient


# TODO: Need add API Access Key. Now i am getting this error (You have not supplied an API Access Key. [Required
#  format: access_key=YOUR_ACCESS_KEY])
def test_currency_client():
    print('1. Initialize the client with a cache duration of 5 minutes')
    client = CurrencyClient(minutes=5)

    print('2. Get the USD currency rate for the first time')
    usd_rate = client.get_currency('USD')

    print('3. Check if the rate is a float number')
    assert isinstance(usd_rate, float)

    print('4. Get the USD currency rate for the second time')
    usd_rate_cached = client.get_currency('USD')

    print('5. Check if the rate is a float number')
    assert isinstance(usd_rate_cached, float)

    print('6. Check if the cached rate is the same as the first one')
    assert usd_rate_cached == usd_rate

    print('7. Set the cache duration to 35 seconds')
    client.set_interval(seconds=35)

    print('8. Get the EUR currency rate')
    eur_rate = client.get_currency('EUR')

    print('9. Check if the rate is a float number')
    assert isinstance(eur_rate, float)

    print('10. Wait for the cache to expire')
    time.sleep(40)

    print('11. Get the EUR currency rate again')
    eur_rate_cached = client.get_currency('EUR')

    print('12. Check if the rate is a float number')
    assert isinstance(eur_rate_cached, float)

    print('13.  Check if the cached rate is different from the first one')
    assert eur_rate_cached != eur_rate
