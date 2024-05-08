from django.urls import path
from . import views


urlpatterns = [
    path('',views.getUsers),
    path('create/', views.registration_view, name= 'create'),
    path('login/',views.login, name='login'),

]