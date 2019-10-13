from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path('', views.analysis),
    path('index', views.index),
    path('generic', views.generic),
    path('elements', views.elements),
    path('downloadingtweets', views.tweetdata),
    path('analysis', views.analysis),
]
