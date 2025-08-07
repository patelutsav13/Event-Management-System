from django.db import models

# Create your models here.

class Events(models.Model):
    eventname = models.CharField(max_length = 150)
    eventdate = models.CharField(max_length = 150)
    location = models.CharField(max_length = 150)
    category = models.CharField(max_length = 150)

    def __str__(self):
        return self.eventname