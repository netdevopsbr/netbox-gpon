from django.urls import path
from . import models, views

urlpatterns = (
    path('', views.HomeView.as_view(), name='home'),
    path('olt', views.OltView.as_view(), name='olt'),
)