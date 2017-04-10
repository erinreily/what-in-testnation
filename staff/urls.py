from django.conf.urls import url

from . import views

app_name = "staff"
urlpatterns = [
    url(r'^new/$', views.new, name='staff_new'),
    url(r'^edit/$', views.edit, name='staff_edit')
]