from django.forms import ModelForm, ValidationError
from app.models import AppOne
import re


class FormAppOne(ModelForm):
    class Meta:
        model = AppOne

    def clean_name(self):
        cleaned_name = self.cleaned_data.get('name')
        if re.findall('\d+', cleaned_name):
            raise ValidationError("Name must be only text")
        return cleaned_name
