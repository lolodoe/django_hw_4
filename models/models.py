from django.db import models
from brands.models import Brand


class Model(models.Model):
    name = models.CharField(max_length=40, verbose_name="Модель машины")
    engine = models.CharField(max_length=60)
    hp = models.IntegerField(null=True)
    nm = models.IntegerField(null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=False)
    photo = models.ImageField(upload_to='photos', null=True)


class Series(models.Model):
    name = models.CharField(max_length=100, verbose_name="серия машины")
    series = models.ForeignKey(Model, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name

