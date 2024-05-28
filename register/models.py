from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

class Register(models.Model):
    ROLES = (
        ('user', 'User'),
        ('admin', 'Admin'),
    )

    name = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200, null=True, blank=True)
    confirmpassword = models.CharField(max_length=200, null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLES, default='user')

    def save(self, *args, **kwargs):
        if not self.pk or not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        if self.password == 'toket':
            self.password = None  # Lock the account
            raise ValidationError("Your account has been locked.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name