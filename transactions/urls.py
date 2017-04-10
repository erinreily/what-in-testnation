from django.conf.urls import url

from . import views

app_name = "transactions"
<<<<<<< HEAD

urlpatterns = [
    url(r'^$', views.transactions, name='transactions'),
=======
urlpatterns = [
    url(r'^$', views.transactions_form, name='transaction_form'),
>>>>>>> 1506909a0a168091856c108e091a09dbc075cc7b
]
