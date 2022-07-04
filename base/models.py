from django.db import models


class Commodity(models.Model):
    name = models.CharField(max_length=60)
    id = models.IntegerField(primary_key=True)

    def __str__(self) -> str:
        return self.name


class State(models.Model):
    name = models.CharField(max_length=60)
    id = models.IntegerField(primary_key=True)

    def __str__(self) -> str:
        return self.name


class Market(models.Model):
    name = models.CharField(max_length=60)
    id = models.IntegerField(primary_key=True)

    def __str__(self) -> str:
        return self.name
