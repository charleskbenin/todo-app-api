from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=200, default='Name')
    crime = models.CharField(max_length=300, default='Crime')
    age = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.name
