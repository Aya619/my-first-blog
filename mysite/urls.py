from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('cal/', views.cal, name='cal'),
    path('liner/', views.liner, name='liner'),
	path('mine/', views.mine, name='mine'),

]