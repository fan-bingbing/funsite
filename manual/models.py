from django.db import models

# Create your models here.
class FEP(models.Model):
    parameter = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    def __str__(self):
        return self.parameter

class ACTION(models.Model):
    action_name = models.CharField(max_length=200)

    def __str__(self):
        return self.action_name

class EQUIPMENT(models.Model):
    equipment_yes = models.CharField(max_length=200)

    def __str__(self):
        return self.equipment_yes
