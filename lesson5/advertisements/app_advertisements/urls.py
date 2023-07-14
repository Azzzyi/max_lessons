from django.urls import path
from .views import ind, top_sellers

urlpatterns = [ 
    path('',ind, name="index"),
    path('top-sellers/',top_sellers, name='top-sellers')
]