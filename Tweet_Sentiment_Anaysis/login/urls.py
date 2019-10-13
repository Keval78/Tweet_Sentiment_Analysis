from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path('', views.login),
    path('auth/', views.auth_view),
    path('logout/', views.logout),
    #path('invalidlogin/', views.invalidlogin),
]

