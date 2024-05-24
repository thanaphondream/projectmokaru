from django.db import models
from django.contrib.auth.hashers import make_password

class Register(models.Model):
    ROLES = (
        ('user', 'User'),
        ('admin', 'Admin'),
    )

    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLES, default='user')

    def save(self, *args, **kwargs):
        if not self.pk: 
            self.password = make_password(self.password)
        super(Register, self).save(*args, **kwargs)

    def __str__(self):
        return self.name