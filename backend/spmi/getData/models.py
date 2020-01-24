from django.db import models

class AuthorID(models.Model):

    scopusID = models.CharField(max_length = 255)
    