from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/result', views.search_result, name='search_result'),
    path('terms/result', views.terms_result, name='terms_result'),
    path('stream/result', views.stream_result, name='stream_result'),
    path('search/api', views.search_api, name='search_api'),
    path('metrics/result', views.metrics_result, name='metrics_resut'),
    path('collection/result', views.collection_result, name='collection_resut'),
    path('search', views.search, name='search'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('metrics', views.metrics, name='metrics'),
]

