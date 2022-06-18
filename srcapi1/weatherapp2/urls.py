
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('apis/', views.api_view, name="api"),
]
