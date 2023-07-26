from django.urls import path
from .views import FetchDataView,GetAllDataView ,display_data

urlpatterns = [
    path('fetch-data/', FetchDataView.as_view(), name='fetch-data'),
    path('get-all-data/', GetAllDataView.as_view(), name='get-all-data'),
    path('display-data/', display_data, name='display_data'),
]
