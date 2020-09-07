from django.db import models
from django.utils import timezone


class AbstractModel(models.Model):

    class Meta:
        abstract = True

    deleted = models.BooleanField(default=False, null=False)
    created_at = models.DateTimeField(default=timezone.now, null=False)
    updated_at = models.DateTimeField(blank=True, null=True)