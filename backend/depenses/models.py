from django.db import models

# Create your models here.
class Depenses(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title