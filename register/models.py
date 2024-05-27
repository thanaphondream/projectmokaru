from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

class Rg(models.Model):
    ROLES = (
        ('user', 'User'),
        ('admin', 'Admin'),
    )

    names = models.CharField(max_length=285, null=True, blank=True)
    emails = models.EmailField(unique=True)
    passwords = models.CharField(max_length=215)
    roles = models.CharField(max_length=15, choices=ROLES, default='user')

    def save(self, *args, **kwargs):
        if not self.pk or not self.passwords.startswith('pbkdf2_sha256$'):
            self.passwords = make_password(self.passwords)
        if self.passwords == 'toket':
            self.passwords = None  # Lock the account
            raise ValidationError("Your account has been locked.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.names


