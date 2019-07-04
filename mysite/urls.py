from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from main.views import about, blog


urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
]
