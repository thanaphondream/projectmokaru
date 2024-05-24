from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    confirmpassword = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
