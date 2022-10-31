from datetime import datetime
from email.policy import default
from django.db import models
import uuid;

GENDER = (
    ('MALE', 'male'),
    ('FEMALE', 'female'),
    ('OTHERS', 'others'),
)

class UserProfile(models.Model):
    user_id = models.CharField(max_length=250, blank=False, default=uuid.uuid1())
    full_name = models.CharField(max_length=250, blank=False, default='')
    user_name = models.CharField(max_length=250, blank=False, default='')
    user_password = models.CharField(max_length=250, blank=False, default='')
    user_gender = models.CharField(max_length=6, choices=GENDER)
    user_birthdate = models.DateTimeField(default=datetime.now, blank=True)