from django.db import models

# Create your models here.
class History(models.Model):
    name = models.CharField(max_length=50)
    user_input = models.TextField()
    output = models.TextField()