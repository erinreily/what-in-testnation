from django import forms
from models import Donation


class DonationForm(forms.Form):
<<<<<<< HEAD
    first_name = forms.CharField(max_length=150, label="First Name", required=False)
    last_name = forms.CharField(max_length=150, label="Last Name", required=False)
    amount = forms.DecimalField(decimal_places=2, label="Amount", required=True)
    card_number = forms.CharField(max_length=16, min_length=16, label="Card Number", required=True)
    message = forms.CharField(max_length=2000, label="Message", required=False)

    class Meta:
        model = Donation
        fields = ('first_name', 'last_name', 'amount', 'card_number', 'message')
=======
    name = forms.CharField(max_length=150, label="Name:", required=True)
    amount = forms.DecimalField(decimal_places=2, label="Amount:", required=True)
    card_number = forms.CharField(max_length=16, label="Card Number:", required=True)

    class Meta:
        model = Donation
        fields = ('name', 'amount', 'card_number', 'message')
>>>>>>> 1506909a0a168091856c108e091a09dbc075cc7b
