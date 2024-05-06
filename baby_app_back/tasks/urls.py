
from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name ="test"),
    path('deleteactivity', views.delete_all_activities_view, name ="delete"),
]