from django.urls import path
from . import views

urlpatterns = [
    path('websocket-test/', views.websocket_test, name='websocket_test'),
]
