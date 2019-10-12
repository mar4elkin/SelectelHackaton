from django import forms

from .widgets import TagsImput


class TagsField(forms.CharField):
    widget = TagsImput
    
    def __init__(self, input_class='flexdatalist', placeholder='', TagModel=None, **kwargs):
        self.widget.input_class = input_class
        self.widget.placeholder = placeholder
        if TagModel:
            self.widget.TagModel = TagModel
        
        super().__init__(**kwargs)
    # def clean(self, value):
    #     try:
    #         return value.upper()
    #     except:
    #         raise ValidationError