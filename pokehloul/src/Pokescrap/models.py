from django.db import models


# Create your models here.
class To_Scrap(models.Model):
    TYPE_CHOICES = [
        ("T", "Talent"),
        ("A", "Attaque"),
        ("P", "Pokemon"),
    ]
    name = models.CharField(max_length=150, default="Unknown")
    type_element = models.CharField(max_length=1, choices=TYPE_CHOICES)
    url = models.CharField(max_length=150)
    is_scraped = models.BooleanField(default=False)