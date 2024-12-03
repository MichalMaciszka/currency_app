from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import OrderingFilter
from .models import Currency, ExchangeRate
from .serializers import CurrencySerializer, ExchangeRateSerializer

class CurrencyListView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['code']
    ordering = ['code']

class ExchangeRateView(APIView):
    def get(self, request, base, target):
        pair_code = f"{base}{target}"
        latest_rate = ExchangeRate.objects.filter(currency_pair=pair_code).order_by('-timestamp').first()

        if latest_rate:
            serializer = ExchangeRateSerializer(latest_rate)
            return Response(serializer.data)
        else:
            return Response(
                {"error": f"Exchange rate for {pair_code} not found."},
                status=status.HTTP_404_NOT_FOUND
            )

