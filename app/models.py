from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=255)    # type: ignore
    lastname = models.CharField(max_length=255)     # type: ignore
    phone = models.IntegerField(null=True)  # type: ignore
    slug = models.SlugField(default="", null=True) #type: ignore

def __str__(self):
    return f"{self.firstname} {self.lastname}"