from django.urls import path
from .views import query, result, history, ping

urlpatterns = [
    path('query/', query, name='query'),
    path('result/', result, name='result'),
    path('history/', history, name='history'),
    path('ping/', ping, name='ping'),
]
