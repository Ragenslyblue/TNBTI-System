from django.db import models

# Create your models here.

class RegisterUser(models.Model):
    email = models.CharField(max_length=200, blank=False)
    username = models.CharField(max_length=200, blank=False)
    firstname = models.CharField(max_length=200, blank=False)
    middlename = models.CharField(max_length=200, blank=False)
    lastname = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.username
