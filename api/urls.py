from django.urls import path
from . import views 

urlpatterns = [
    path('querydata/', views.getQueryData),
    path('cropdata/', views.getCropData)
]
