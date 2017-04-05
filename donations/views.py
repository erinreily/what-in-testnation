from django.shortcuts import render
from django.template import Context
from models import Donation

from forms import DonationForm
from django.views.decorators.csrf import csrf_protect, csrf_exempt


@csrf_exempt
def donations_form(request):
    form = DonationForm(request.POST or None)
    context = Context({
        'donated': False,
        'form': form
    })
    if request.method == 'POST' and form.is_valid():
        data = request.POST
        new_donation = Donation(name=data.get('name'),
                                amount=data.get('amount'),
                                card_number=data.get('card_number'),
                                message=data.get('message'))
        new_donation.save()
        context['donated'] = True
        return render(request, "donations/donation_form.html", context)
    else:
        return render(request, "donations/donation_form.html", {'donated': False,
                                                                'form': form})
