from django.db import models

class Car(models.Model):
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.model