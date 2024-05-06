from django.urls import path
from . import views


urlpatterns = [
    path('',views.getUsers),
    path('create/', views.registration_view, name= 'create'),

]