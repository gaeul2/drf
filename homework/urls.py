from django.urls import path
from . import views

urlpatterns = [
    path('homework/', views.UserView.as_view(), name="make_some")
]