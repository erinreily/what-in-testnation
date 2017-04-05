from django.conf.urls import url

from . import views

app_name = "donations"
urlpatterns = [
    url(r'^$', views.donations_form, name='donations_form')
]