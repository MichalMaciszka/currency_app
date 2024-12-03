from django.test import TestCase
from .models import Currency, ExchangeRate


class CurrencyAPITests(TestCase):
    def setUp(self):
        Currency.objects.create(code='USD')

    def test_get_currencies(self):
        response = self.client.get('/api/currency/')
        self.assertEqual(response.status_code, 200)
        self.assertIn({'code': 'USD'}, response.json())

    def test_get_exchange_rate(self):
        ExchangeRate.objects.create(currency_pair='EURUSD', exchange_rate=1.1)
        response = self.client.get('/api/currency/EUR/USD/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['exchange_rate'], 1.1)

    def test_get_latest_exchange_rate(self):
        ExchangeRate.objects.create(currency_pair='EURUSD', exchange_rate=1.1)
        ExchangeRate.objects.create(currency_pair='EURUSD', exchange_rate=1.2)
        response = self.client.get('/api/currency/EUR/USD/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['exchange_rate'], 1.2)

