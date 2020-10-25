from django.forms import ModelForm
from .models import OrderItem


class orderItemForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = ['signature', 'printstyle', 'other']
