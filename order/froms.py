from django import forms


class ItemAddForm(forms.Form):
    quantity = forms.CharField()