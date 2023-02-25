from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'member/', views.member, name='member'),

    path(r'group/', views.group, name='group'),

    # API
    path(r'data/members/', views.get_members, name='get_members'),
]