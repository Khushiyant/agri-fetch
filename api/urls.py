from django.urls import path
from . import views 

urlpatterns = [
    path('', views.getQueryData),
    path('query', views.getQueryData),
]
