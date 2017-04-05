from django.conf.urls import url
from . import views


app_name = "manager"

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^registration$', views.registration, name="registration"),
	url(r'^register$', views.register, name="register"),
	url(r'^login$', views.login, name="login"),
	url(r'^home$', views.home, name="home"),
	url(r'^success$', views.success, name="success"),
    url(r'^logout$', views.logout, name="logout"),
]
