# Generated by Django 5.0.2 on 2024-03-17 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0005_jobpost_expiry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobpost',
            old_name='expiry',
            new_name='Job_expiry_date',
        ),
    ]