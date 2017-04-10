from django.shortcuts import render
<<<<<<< HEAD
from django.utils import timezone
from models import Donation

=======
from django.template import Context
from models import Donation

from forms import DonationForm
>>>>>>> 1506909a0a168091856c108e091a09dbc075cc7b
from django.views.decorators.csrf import csrf_protect, csrf_exempt


@csrf_exempt
def donations_form(request):
<<<<<<< HEAD
    if request.method == 'POST':
        data = request.POST
        new_donation = Donation(first_name=data.get('first_name'),
                                last_name=data.get('last_name'),
                                amount=data.get('amount'),
                                card_number=data.get('card_number'),
                                cvv=data.get('cvv'),
                                message=data.get('message'),
                                donation_made=timezone.now())
        new_donation.save()
        return render(request, "donations/donation_form.html", {'donated': True})
    else:
        return render(request, "donations/donation_form.html", {'donated': False})
=======
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
>>>>>>> 1506909a0a168091856c108e091a09dbc075cc7b
