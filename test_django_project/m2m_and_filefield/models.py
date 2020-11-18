from django.db import models


class A(models.Model):
    name = models.CharField(max_length=20)


class B(models.Model):
    name = models.CharField(max_length=20)
    file = models.FileField()
    a_field = models.ManyToManyField(A, blank=True, related_name='bs')
