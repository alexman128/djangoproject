from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=254)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Channel(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class BackendUser(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=254, null=True)
    phone = PhoneNumberField(null=True)
    categories = models.ManyToManyField(Category)
    channels = models.ManyToManyField(Channel)

    def __str__(self):
        return f"{self.name}"


