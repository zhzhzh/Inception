from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^member/$', views.member, name='member'),

    url(r'^group/$', views.group, name='group'),

    # API
    url(r'^data/members/$', views.get_members, name='get_members'),
]