from django.db import models

class personalData(models.Model):

    index = models.AutoField(primary_key=True)
    surname = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)
    link = models.CharField(max_length = 255)
    academicDegree = models.CharField(max_length = 255)
    position = models.CharField(max_length = 255)
    department = models.CharField(max_length = 255)