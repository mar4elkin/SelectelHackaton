from django.db                  import models
from django.urls                import reverse
from django.utils               import timezone
from django.utils.translation   import ugettext_lazy as _

from taggit.managers            import TaggableManager
from taggit.models              import TagBase, TaggedItemBase, GenericUUIDTaggedItemBase

import uuid
