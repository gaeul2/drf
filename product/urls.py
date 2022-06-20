from django.urls import path
from . import views


urlpatterns = [
    path('event', views.EventView.as_view(), name='create_event'),
    path('update/event/<int:event_id>', views.UpdateEvent.as_view(), name= 'update_event'),
]