from django import forms

from django.core.exceptions     import ValidationError
from django.utils.translation   import ugettext_lazy as _
import                                 datetime

from selectelhackaton.coreApp.models import Task
class MainTaskForm(forms.Form):
    title = forms.CharField(label='Название', max_length=100)
    deadline = forms.DateTimeField()

    description = forms.CharField(label='Описание', widget=forms.Textarea)