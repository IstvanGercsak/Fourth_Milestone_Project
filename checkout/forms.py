from django import forms
from .models import Order


class MakePaymentForm(forms.Form):
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2036)]

    credit_card_number = forms.IntegerField(label='Credit card number', required=True)
    cvv = forms.IntegerField(label='Security code (CVV)', required=True, max_value=999)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

    def clean_credit_card_number(self):
        credit_card_number = self.cleaned_data.get("credit_card_number")
        return self.clean_credit_card_number()


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            # 'full_name',
            # 'phone_number',
            # 'country',
            # 'postcode',
            # 'town_or_city',
            # 'street_address1',
            # 'street_address2',
            'county',
        )
