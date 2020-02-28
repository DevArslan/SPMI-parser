from django.db import models

class scopusData(models.Model):

    index = models.AutoField(primary_key=True)
    author = models.CharField(max_length = 255)
    creator = models.CharField(max_length = 255)
    title = models.CharField(max_length = 255)
    journal = models.CharField(max_length = 255)
    date = models.CharField(max_length = 255)
    volume = models.CharField(max_length = 255)
    issue = models.CharField(max_length = 255)
    pages = models.CharField(max_length = 255)
    doi = models.CharField(max_length = 255)
