from django.urls import path
from hll1 import views

urlpatterns = [
    path('', views.hll, name='hll'),
]
