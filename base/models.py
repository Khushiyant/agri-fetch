from django.db import models

class Commodity(models.Model):
    name = models.CharField(max_length=60)
    id = models.IntegerField()

class State(models.Model):
    name = models.CharField(max_length=60)
    id = models.IntegerField()

class Market(models.Model):
    name = models.CharField(max_length=60)
    id = models.IntegerField()