from django.urls import path
from . import views


urlpatterns = [
    path('create/event', views.CreateEvent.as_view(), name='create_event'),
]