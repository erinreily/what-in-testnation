from django.conf.urls import url

from . import views

app_name = "member"
urlpatterns = [
    url(r'^new/$', views.new, name='member_new'),
    url(r'^login/', views.member_login, name='member_login'),
    url(r'^edit/$', views.edit, name='member_edit')
]