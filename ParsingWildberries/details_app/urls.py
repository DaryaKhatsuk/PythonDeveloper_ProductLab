from django.urls import path
from .views import product_info, error

urlpatterns = [
    path('', product_info, name='product_info'),
    path('error/', error, name='error'),
]
