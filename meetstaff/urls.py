from django.conf.urls import url

from . import views

app_name="meetstaff"
urlpatterns = [
    url(r'^$', views.staff_table, name='staff_table'),
]
