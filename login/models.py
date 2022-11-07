from datetime import datetime
from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid;

class UserProfile(AbstractUser):
    user_id = models.CharField(max_length=250, blank=True, default=uuid.uuid1())
    full_name = models.CharField(max_length=250, blank=False, default='')
    user_gender = models.CharField(max_length=6, blank=False, default='male')
    user_birthdate = models.DateTimeField(default=datetime.now, blank=True)
    user_address = models.CharField(max_length=250, blank=True, default='')
    user_phone = models.CharField(max_length=250, blank=True, default='')
    user_icon = models.CharField(max_length=250, blank=True, default='')

    REQUIRED_FIELDS = []

    def __str__(self):
        return self

    class Meta:
        managed = True
        db_table = 'userprofile'