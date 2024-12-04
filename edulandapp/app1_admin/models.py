from django.db import models

# Create your models here.
class Mainpage(models.Model):
    Name=models.CharField(max_length=250)
    Number=models.IntegerField(null=True)
    Description=models.TextField()
