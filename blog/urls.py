#from django.urls import path, re_path

from django.conf.urls import url

from . import views

urlpatterns = [

	url(r'^$', views.post_list, name='post_list'),
]