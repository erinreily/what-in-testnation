from django import forms
from models import Donation


class DonationForm(forms.Form):
    name = forms.CharField(max_length=150, label="Name:", required=True)
    amount = forms.DecimalField(decimal_places=2, label="Amount:", required=True)
    card_number = forms.CharField(max_length=16, label="Card Number:", required=True)

    class Meta:
        model = Donation
        fields = ('name', 'amount', 'card_number', 'message')
