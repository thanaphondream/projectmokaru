# Generated by Django 5.0.6 on 2024-05-27 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_rename_email_register_emails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='emails',
            new_name='email',
        ),
    ]