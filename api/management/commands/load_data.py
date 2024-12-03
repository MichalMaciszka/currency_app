from django.core.management.base import BaseCommand
from api.models import Currency, ExchangeRate
import yfinance as yf
from datetime import datetime

class Command(BaseCommand):
    help = 'Load data from Yahoo Finance API'

    def handle(self, *args, **kwargs):
        currencies = ['EUR', 'USD', 'JPY', 'PLN']
        for code in currencies:
            Currency.objects.get_or_create(code=code)

        pairs = [('EUR', 'USD'), ('USD', 'JPY'), ('PLN', 'USD')]
        for base, target in pairs:
            pair_code = f"{base}{target}"
            ticker = yf.Ticker(pair_code + "=X")
            hist = ticker.history(period="1d")

            if not hist.empty:
                rate = hist['Close'][0]
                timestamp = datetime.now()
                
                ExchangeRate.objects.create(
                    currency_pair=pair_code,
                    exchange_rate=rate,
                    timestamp=timestamp
                )

                self.stdout.write(self.style.SUCCESS(
                    f"Saved historical rate for {pair_code}: {rate} at {timestamp}"
                ))
            else:
                self.stdout.write(self.style.WARNING(f"No data found for {pair_code}"))

        self.stdout.write(self.style.SUCCESS('Data loading complete!'))
