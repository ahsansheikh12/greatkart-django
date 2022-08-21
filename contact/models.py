from dataclasses import dataclass
import email
from unicodedata import category
from django.db import models

# Create your models here.
class ContactData(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200,blank=False)
    messagenote=models.TextField(max_length=500,blank=False)

    def __str__(self):
        return self.name

        