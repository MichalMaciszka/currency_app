from django.urls import path
from .views import CurrencyListView, ExchangeRateView

urlpatterns = [
    path('currency/', CurrencyListView.as_view(), name='currency-list'),
    path('currency/<str:base>/<str:target>/', ExchangeRateView.as_view(), name='exchange-rate'),
]
