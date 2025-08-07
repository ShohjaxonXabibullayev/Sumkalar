from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=52)

    def __str__(self):
        return self.name

class Sumkalar(models.Model):
    name = models.CharField(max_length=120)
    type = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    made_country = models.CharField(max_length=120)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name