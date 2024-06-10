from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('profile', views.profile, name='profile'),
    path('register', views.registration, name='register'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
