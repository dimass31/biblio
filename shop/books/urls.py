from django.conf.urls import url, include
from django.contrib import admin
from books import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^books/$', views.landing, name='books'),
]