from django.db import models

# Create your models here.
class DogModel(models.Model):
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"