from django.db import models

class articleData(models.Model):

    index = models.AutoField(primary_key=True)
    spmiProfileLink = models.CharField(max_length = 255)
    rsciID = models.CharField(max_length = 255)
    spinID = models.CharField(max_length = 255)
    scopusID = models.CharField(max_length = 255)
    researcherID = models.CharField(max_length = 255)
    orcidID = models.CharField(max_length = 255)

    rsciProfileLink = models.CharField(max_length = 255)
    scopusProfileLink = models.CharField(max_length = 255)
    publonsProfileLink = models.CharField(max_length = 255)
    orcidProfileLink = models.CharField(max_length = 255)
    researchProfileLink = models.CharField(max_length = 255)
    scholarProfileLink = models.CharField(max_length = 255)
