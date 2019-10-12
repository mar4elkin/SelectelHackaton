from django.db                  import models
from django.urls                import reverse
from django.utils               import timezone
from django.utils.translation   import ugettext_lazy as _

from taggit.managers            import TaggableManager
from taggit.models              import TagBase, TaggedItemBase, GenericUUIDTaggedItemBase

import uuid

from selectelhackaton.auth.models import User

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


class Task(models.Model):
    """ Это задачи (компания) """
    
    STATUS_LIST = [
        ('WH', 'В ожидание'),
        ('CH', 'На модерации'),
        ('IP', 'В разработке'),
        ('RD', 'Готово'),
    ]

    title = models.CharField(max_length=100)

    created_date = models.DateTimeField(auto_now=True)

    description = models.TextField()

    deadline = models.DateTimeField(null=True, blank=True)

    tags = TaggableManager()

    updated_data = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(User, verbose_name=("Создатель"), on_delete=models.CASCADE)

    is_internal = models.BooleanField(
        _('Для внутреннего пользования'), 
        default=False,
        help_text=_("Является ли задача для внутреннего пользования.")
    )

    status = models.CharField(
        max_length = 2,
        choices = STATUS_LIST,
        default = 'WH',
    )

class Squad(models.Model):
    """ Это группы (компания) """

    description = models.TextField()

    teammates = models.ManyToManyField(User)
    
    #rating = models.IntegerField(max_length=10)

    @property
    def teammate_str(self):
        return ", ".join(
            [teammate.name for teammate in teammates]
            )