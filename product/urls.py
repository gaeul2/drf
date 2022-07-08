from django.urls import path
from . import views

app_label = 'product'

urlpatterns = [
    path('event', views.EventView.as_view(), name='create_event'),
    path('update/event/<int:event_id>', views.UpdateEvent.as_view(), name= 'update_event'),
    path('thumbnail/<int:obj_id>', views.EventThumbnailView.as_view(), name='show_thumbnail'),
]