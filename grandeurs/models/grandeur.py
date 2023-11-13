from django.db import models


class Grandeur(models.Model):
    nom = models.CharField(max_length = 50)
    unite = models.CharField(max_length = 30)
    valeurMin = models.FloatField()
    valeurMax = models.FloatField()

    def __str__(self) :
        return f'Grandeur: { self.nom }, Unit: {self.unite} et valeurs entre {self.valeurMin} et {self.valeurMax}'
    