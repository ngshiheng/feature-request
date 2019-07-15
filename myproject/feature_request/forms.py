import datetime
from django.core.exceptions import ValidationError
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Request


class DateInput(forms.DateInput):
    input_type = 'date'


class RequestForm(forms.ModelForm):
    def clean_target_date(self):
        data = self.cleaned_data['target_date']

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - target date in past'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data

    class Meta:
        model = Request
        fields = '__all__'
        widgets = {
            'target_date': DateInput(),
        }
