from django import forms


class CartForm(forms.Form):
    quantity = forms.IntegerField()