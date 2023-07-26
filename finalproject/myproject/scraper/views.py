import logging
import colorlog
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from bs4 import BeautifulSoup
from .models import StockData
from .serializers import StockDataSerializer

# Configure logging for success events
success_logger = logging.getLogger('success_logger')
success_handler = logging.FileHandler('success.log')
success_logger.addHandler(success_handler)
success_logger.setLevel(logging.INFO)

# Configure logging for failure events
failure_logger = logging.getLogger('failure_logger')
failure_handler = logging.FileHandler('failure.log')
failure_logger.addHandler(failure_handler)
failure_logger.setLevel(logging.ERROR)


def get_data_from_yahoo_finance():
    url = 'https://finance.yahoo.com/lookup'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.select_one('.trending-table')
        rows = table.select('tbody tr')
        all_data = []
        for row in rows:
            symbol = row.select_one('.data-col0 a').text
            name = row.select_one('.data-col1').text
            last_price = row.select_one('.data-col2').text
            change = row.select_one('.data-col3').text
            percentage_change = row.select_one('.data-col4').text
            all_data.append({
                'symbol': symbol,
                'name': name,
                'last_price': last_price,
                'change': change,
                'percentage_change': percentage_change,
            })
        return all_data
    return []


class FetchDataView(APIView):
    def post(self, request):
        data = get_data_from_yahoo_finance()
        if not data:
            failure_logger.error('Failed to fetch data from Yahoo Finance lookup')
            return Response({"error": "Failed to fetch data from Yahoo Finance lookup."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = StockDataSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()

            success_logger.info('Data successfully fetched and stored.')
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        failure_logger.error('Failed to save data to the database.')
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetAllDataView(APIView):
    def get(self, request):
        data = StockData.objects.all()
        serializer = StockDataSerializer(data, many=True)
        return Response(serializer.data)


def display_data(request):
    return render(request, 'rest_framework/all_data_list.html')

# class GetAllDataView(APIView):
#     def get(self, request):
#         data = StockData.objects.all()
#         serializer = StockDataSerializer(data, many=True)
#         context = {'data': serializer.data}
#         return render(request, 'rest_framework/data_list.html', context)
