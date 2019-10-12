from django import forms
from django.forms import widgets
from django.conf import settings

from taggit.models import Tag, TaggedItem

class TagsImput(widgets.TextInput):
    input_type = 'text'
    template_name = 'tags/forms/widgets/tags_input.html'

    input_class = 'flexdatalist'
    placeholder = ''

    TagModel = Tag

    def render(self, name, value, attrs=None, choices=(), renderer=None):
        """Render the widget as an HTML string."""
        context = self.get_context(name, value, attrs)
        context['STATIC_URL'] = settings.STATIC_URL
        context['input_class'] = self.input_class
        context['placeholder'] = self.placeholder
        context['tag_list'] = self.TagModel.objects.all()

        return self._render(self.template_name, context, renderer)