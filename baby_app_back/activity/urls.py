from django.urls import path
from .views import getActivities, getActivity, createActivity, activityUpdate

urlpatterns = [
    path('', getActivities, name='activities'),
    path('create/', createActivity, name='activity-create'),
    path('get/<str:pk>/', createActivity, name='activity-get'),
    path('update/<str:pk>/', activityUpdate, name='activity-update'),

]