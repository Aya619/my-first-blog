from django.urls import path
from . import views



urlpatterns = [
    path('', views.prop, name='prop'),
]