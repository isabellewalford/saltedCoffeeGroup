import datetime
from django.utils import timezone

from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User, Permission


class Plant(models.Model):
    plant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class PlantOfTheDay(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        today = timezone.now().date()
        existing_instance = PlantOfTheDay.objects.filter(date=today).first()
        if existing_instance:
            existing_instance.plant = self.plant
            super(PlantOfTheDay, existing_instance).save(*args, **kwargs)
        else:
            super(PlantOfTheDay, self).save(*args, **kwargs)

    def __str__(self):
        return self.plant.name
