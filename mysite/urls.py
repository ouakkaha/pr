from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.conf.urls import include, url

urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('admin/', admin.site.urls),
    path('', include('main.urls/views')),
]
