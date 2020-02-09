from django.db import models

# Create your models here.
class FORMNAME(models.Model):
    NAME=models.CharField(max_length=25)
    EMAIL=models.EmailField()
    PASSWORD=models.CharField(max_length=25)
    def __str__(self):
        return self.EMAIL