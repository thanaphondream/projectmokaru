from django.db import models

class Address(models.Model):
    name = models.CharField(null=True, blank=True, max_length=255)
    phone = models.IntegerField(null=True, blank=True, max_length=15)
    province = models.TextField(null=True, blank=True, max_length=50)
    district = models.TextField(null=True, blank=True, max_length=50)
    tabun  = models.TextField(null=True, blank=True, max_length=50)
    detel  = models.TextField(null=True, blank=True, max_length=50)
    postcode = models.IntegerField(null=True, blank=True, max_length=10)
    road = models.TextField(null=True, blank=True, max_length=50)
    village = models.IntegerField(null=True, blank=True, max_length=80)
    other = models.TextField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.title
