from django.urls import path
from .views import getActivity, createActivity

urlpatterns = [
    path('', getActivity, name='activities'),
    path('create/', createActivity, name='activity-create'),
]