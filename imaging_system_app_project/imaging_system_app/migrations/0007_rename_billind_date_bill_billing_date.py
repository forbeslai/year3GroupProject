# Generated by Django 3.2 on 2022-01-09 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imaging_system_app', '0006_auto_20220109_0139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill',
            old_name='billind_date',
            new_name='billing_date',
        ),
    ]
