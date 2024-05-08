from django.urls import path
from .views import getUsers, registration_view

urlpatterns = [
    path('users/', getUsers, name='get_users'),
    path('register/', registration_view, name='register'),
]