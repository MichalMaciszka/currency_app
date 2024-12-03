from django.contrib import admin
from .models import Currency, ExchangeRate

# Register your models here.
@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'code')

@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('currency_pair', 'exchange_rate', 'timestamp')
    list_filter = ('currency_pair', 'timestamp')
    search_fields = (['currency_pair'])
    ordering = (['-timestamp'])

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if 'currency_pair' in request.GET:
            queryset = queryset.filter(currency_pair=request.GET['currency_pair'])
        return queryset

