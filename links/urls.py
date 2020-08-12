from django.urls import path

from . import views


urlpatterns = [
    path('', views.link_list, name='link_list'),
    path('', views.link_list, name='index'),
    path('create/', views.link_create, name='link_create'),
    path('link_clicked/', views.link_clicked, name='link_clicked'),
    path('appearance/', views.link_list, name='appearance'),
    path('stats/', views.stats, name='stats'),
    path('settings/', views.settings, name='settings'),
]


