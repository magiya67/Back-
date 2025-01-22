from django.urls import path
from . import views

urlpatterns = [
    path('', views.another_serv_request),
]