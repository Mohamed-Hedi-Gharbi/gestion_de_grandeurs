from django.db import models

class Mesure(models.Model):
    value = models.FloatField()
    dateMesure = models.DateTimeField()
    grandeur = models.ForeignKey('Grandeur', on_delete = models.CASCADE)


    def __str__(self):
        return f'Mesure: {self.value} at {self.dateMesure}'
