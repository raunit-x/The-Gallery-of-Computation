from django.forms import ModelForm
from django.forms import widgets
from .models import OrderItem, ShippingAddress
from django import forms


class orderItemForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = ['signature', 'printstyle', 'other']


class ShippingAddressForm(ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['name', 'email', 'address1', 'address2', 'country', 'postal', 'city', 'state']
        widgets = {
            'email': forms.TextInput(attrs={'type': 'email', 'name': 'email', 'placeholder': 'Email'}),
            'name': forms.TextInput(attrs={'type': 'text', 'name': 'name', 'placeholder': 'Name'}),
            'address1': forms.TextInput(attrs={'type': 'text', 'name': 'address', 'placeholder': 'Address 1'}),
            'address2': forms.TextInput(attrs={'type': 'text', 'name': 'address', 'placeholder': 'Address 2'}),
            'country': forms.TextInput(attrs={'type': 'text', 'name': 'country', 'placeholder': 'Country'}),
            'postal': forms.TextInput(attrs={'type': 'text', 'name': 'postal', 'placeholder': 'Postal'}),
            'city': forms.TextInput(attrs={'type': 'text', 'name': 'city', 'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'type': 'text', 'name': 'state', 'placeholder': 'State'}),
        }
