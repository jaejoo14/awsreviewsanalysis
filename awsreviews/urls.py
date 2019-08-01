from django.urls import path
from . import views

urlpatterns = [
    path('', views.query_list, name='query_list'),
]

