from django.urls import path
from .views import *
# urls.py
urlpatterns = [
    path("",index,name='index'),
]
