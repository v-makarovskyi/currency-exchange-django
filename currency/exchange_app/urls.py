from django.urls import path
from .views import exchange

app_name = 'exchange_app'

urlpatterns = [
    path('', exchange, name='exchange')
]