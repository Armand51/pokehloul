from django.db import models

# Create your models here.

class Pokemon(models.Model):
    name = models.CharField(max_length=150)
    url = models.CharField(max_length=150)
    picture_url = models.CharField(max_length=150, default='')

    
class Talent(models.Model):
    name = models.CharField(max_length=150)
    url = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    effet_combat = models.CharField(max_length=150, default='')
    effet_terrain = models.CharField(max_length=150, default='')

    
class Attaque(models.Model):
    name = models.CharField(max_length=150)
    url = models.CharField(max_length=150)
