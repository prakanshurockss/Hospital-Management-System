# Generated by Django 3.0.3 on 2021-07-03 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0011_auto_20210630_1742'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='patient',
            new_name='patient_history',
        ),
    ]
