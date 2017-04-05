# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import Context

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def transactions_form(request):
    #return HttpResponse("You have reached the Transactions page.")
    return render(request, "transactions/transactions.html")
