from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
""" Django model class to store the Categories. It has a many to many relationship
    with the BackendUser model class."""


class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=254)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


""" Django model class to store the Channels. It has a many to many relationship
    with the BackendUser model class."""


class Channel(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=254)

    def __str__(self):
        return self.name


""" Django model class to store the Users."""


class BackendUser(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=254, null=True)
    phone = PhoneNumberField(null=True)
    categories = models.ManyToManyField(Category)
    channels = models.ManyToManyField(Channel)

    def __str__(self):
        return f"{self.name}"


""" Django model class to store the info for the messages sent (simulating the actual sending)."""


class MessageSent(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    message_content = models.TextField()
    # All the channels on which the message was sent
    channels = models.ManyToManyField(Channel)
    sent_at = models.DateTimeField(auto_now_add=True)
    # User id which can be used later to retrieve the rest of the info from the user Table
    user = models.ForeignKey(BackendUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.sent_at} - {self.category} - {self.user}"
