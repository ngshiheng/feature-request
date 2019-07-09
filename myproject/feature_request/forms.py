from django import forms
from django.forms import ModelForm

from .models import Request


class DateInput(forms.DateInput):
    input_type = 'date'


class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ['title', 'description', 'client', 'priority', 'target_date', 'product_area']
        widgets = {
            'target_date': DateInput(),
        }
