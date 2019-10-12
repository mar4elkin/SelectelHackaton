from django.db                  import models
from django.urls                import reverse
from django.utils               import timezone
from django.utils.translation   import ugettext_lazy as _
from django.urls                import reverse

from taggit.managers            import TaggableManager
from taggit.models              import TagBase, TaggedItemBase, GenericUUIDTaggedItemBase

import uuid

from selectelhackaton.auth.models import User


class Task(models.Model):
    """ Это задачи (компания) """
    
    # массив статусов
    STATUS_LIST = [
        ('WH', 'В ожидание'),
        ('CH', 'На модерации'),
        ('IP', 'В разработке'),
        ('RD', 'Готово'),
    ]

    # массив сложность
    COMPLEXITY_LIST = [
        ('ES', 'Легко'),
        ('NM', 'Нормально'),
        ('HD', 'Сложно'),
    ]

    # массив важность
    IMPORTANCE_LIST = [
        ('NT', 'Не важно'),
        ('NI', 'Средняя важность'),
        ('IM', 'Важно'),
        ('VI', 'Очень важно'),
    ]

    title = models.CharField(_('Название'),max_length=100)

    created_date = models.DateTimeField(auto_now=True)

    description = models.TextField(_('Описание'))

    deadline = models.DateField(_('Крайний срок'),null=True, blank=True)

    tags = TaggableManager(_('Теги'))

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

    complexity = models.CharField(
        max_length = 2,
        choices = COMPLEXITY_LIST,
        default = 'ES',
    )

    importance = models.CharField(
        max_length = 2,
        choices = IMPORTANCE_LIST,
        default = 'NT',
    )

    class Meta:
        """Meta definition for Order."""

        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')

    @property
    def tags_list(self):
        return ", ".join(o.name for o in self.tags.all())
    
    def __str__(self):
        """Unicode representation of Order."""
        return self.title

    def get_absolute_url(self):
        return reverse('task_ditail', args=[str(self.id)])
    
    def is_available(self, user):
        squads = user.user_squads.all()

        if user == self.author:
            return False

        for squad in squads:
            teammates = squad.teammates
            for teammate in teammates:
                if teammate == self.author:
                    return False
        
        return True
        

class Squad(models.Model):
    """ Это группы (компания) """

    description = models.TextField()

    teammates = models.ManyToManyField(User, related_name='user_squads')
    
    tasks = models.ManyToManyField(Task, related_name='task_squads')
    #rating = models.IntegerField(max_length=10)

    @property
    def teammate_str(self):
        return ", ".join(
            [teammate.name for teammate in self.teammates]
            )