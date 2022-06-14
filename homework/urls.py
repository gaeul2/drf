from django.urls import path
from . import views

urlpatterns = [
    path('homework', views.SongView.as_view(), name="make_some")
]