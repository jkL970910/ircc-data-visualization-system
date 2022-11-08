from django.db import models
import uuid;

class Plan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    plan_name = models.CharField(max_length=250, blank=True, unique=True, default="free")
    plan_price = models.CharField(max_length=250, blank=True, default="0")

    class Meta:
        managed = True
        db_table = 'plan'