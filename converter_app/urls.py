from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("submitquery", views.submitquery, name="submitquery"),
] 