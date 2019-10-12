from django import forms
from django.forms import ModelForm
from django.core.exceptions     import ValidationError
from django.utils.translation   import ugettext_lazy as _
import                                 datetime

from selectelhackaton.coreApp.models import Task

class DateInput(forms.DateInput):
    input_type = 'date'


class MainTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline']
        widgets = {
            'deadline': DateInput(),
        }
