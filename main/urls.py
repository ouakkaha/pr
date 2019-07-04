from django.urls import path
from . import views
from main import views as main_views
from django.contrib.auth import views as auth_views
from main.views import blog, about
from django.conf.urls import include, url

urlpatterns = [
    path('about/', about, name='about'),
    path('', blog, name='blog'),
]
