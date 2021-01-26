from django.conf.urls import url
from django.contrib import admin
from web import views
urlpatterns = [
    url(r'^register/$',views.register),
    url(r'^login/$',views.login),
    url(r'^check_code/$',views.check_code),
    url(r'^get_code/$',views.get_code),
    url(r'^check_user/$',views.check_user),
    url(r'^logout/$',views.logout),
    url(r'^article/(\d+)$',views.article,name='index'),
    url(r'^$', views.index),
]