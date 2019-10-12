from django import forms

from django.core.exceptions     import ValidationError
from django.utils.translation   import ugettext_lazy as _
import                                 datetime

from selectelhackaton.tags.fields           import TagsField

class TagForm(forms.Form):
    tags = TagsField()