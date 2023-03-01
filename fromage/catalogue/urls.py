from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path("cheese/<int:id>", views.cheese_details, name="cheese_details")
]