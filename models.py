from django.db import models
from datetime import date

gender_list =(('M', 'Male'), ('F', 'Female'))
# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, null=True, blank=True, choices=gender_list)
    birthday = models.DateField(default=date.today)
    email = models.EmailField(max_length=50, null=True, blank=True, unique=True)
    favouriteURL = models.URLField(blank=True)
    desc = models.TextField(max_length=500, blank=True)
    photo = models.FileField(blank=True)
    def __str__(self):
        return '%s'%self.name
