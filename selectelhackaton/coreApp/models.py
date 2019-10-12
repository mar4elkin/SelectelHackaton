from django.db                  import models
from django.urls                import reverse
from django.utils               import timezone
from django.utils.translation   import ugettext_lazy as _

from taggit.managers            import TaggableManager
from taggit.models              import TagBase, TaggedItemBase, GenericUUIDTaggedItemBase

import uuid


class Order(models.Model):
    """ Это заказ """

    title = models.TextField()
    
    created_date = models.DateTimeField(auto_now=True)

    discription = models.TextField()

    deadline = models.DateTimeField(null=True, blank=True)

    tags = TaggableManager()

    # TODO: Define fields here

    class Meta:
        """Meta definition for Order."""

        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')

    def __str__(self):
        """Unicode representation of Order."""
        return self.title
