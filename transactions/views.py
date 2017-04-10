# -*- coding: utf-8 -*-
from __future__ import unicode_literals
<<<<<<< HEAD
=======
from django.template import Context
>>>>>>> 1506909a0a168091856c108e091a09dbc075cc7b

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


<<<<<<< HEAD
def transactions(request):
    return render(request, "transactions/transactions.html")

=======
def transactions_form(request):
    return HttpResponse("You have reached the Transactions page.")
    #return render(request, "transactions/transactions.html")
>>>>>>> 1506909a0a168091856c108e091a09dbc075cc7b
