from django.conf.urls import url

from . import views
<<<<<<< HEAD
app_name="home"
=======

>>>>>>> 1506909a0a168091856c108e091a09dbc075cc7b
urlpatterns = [
    url(r'^$', views.index, name='index')
]
