from django.urls import path
from . import views 

urlpatterns = [
    # path('', views.getData),
    path('query/', views.getQueryData),
    path('commodities/', views.getQueryData_commodity),
    path('state/', views.getQueryData_state),
    path('market/', views.getQueryData_market),
]
