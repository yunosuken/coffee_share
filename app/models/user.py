from django.db import models
from .abstract import AbstractModel


class User(AbstractModel):

    class Meta:
        db_table = 'users'

    user_name = models.CharField(max_length=1024, blank=False, null=False)
    mail_address = models.EmailField(max_length=255, null=False)
    password = models.CharField(max_length=128, blank=False, null=False)