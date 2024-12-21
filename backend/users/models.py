from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class CustomUser(models.Model):
    pseudo = models.TextField()
    firstname = models.TextField()
    lastname = models.TextField()
    téléphone = models.TextField()
    email = models.EmailField(unique=True)
    password = models.TextField()

    def save(self, *args, **kwargs):
        if self.pk is None: 
            self.password = make_password(self.password)
            super().save(*args, **kwargs)

    def __str__(self):
        return self.firstname