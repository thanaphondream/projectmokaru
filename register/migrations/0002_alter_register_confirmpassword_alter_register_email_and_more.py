# Generated by Django 5.0.6 on 2024-05-22 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='confirmpassword',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]