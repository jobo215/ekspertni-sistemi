from django.db import models

class Vino(models.Model):

    naziv = models.CharField(max_length=50)
    boja = models.CharField(max_length=50)
    suvoca = models.CharField(max_length=50)
    tekstura = models.CharField(max_length=50)
    aromaticno = models.BooleanField()
    dezertno = models.BooleanField()
    penusavo = models.BooleanField()
