from django.conf.urls import url
from . import views

app_name = "courses"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add$', views.add, name="add"),
    url(r'^join/(?P<id>\d+)$', views.join, name="join"),
    url(r'^edit/(?P<id>\d+)$', views.edit, name="edit"),
    url(r'^drop/(?P<id>\d+)$', views.drop, name="drop"),
    url(r'^remove/(?P<id>\d+)$', views.remove, name="remove"),
    url(r'^confirm/(?P<id>\d+)$', views.confirm, name="confirm"),

]
