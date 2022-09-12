from django.urls import path
from . import views 

urlpatterns = [
    path('cropdata/', views.getQueryData)
]
