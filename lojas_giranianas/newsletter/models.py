from django.db import models

# Create your models here.
class Newsletter(models.Model):
    email = models.EmailField(max_length=75)
    status = models.BooleanField(default=True)

