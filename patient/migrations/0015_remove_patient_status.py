# Generated by Django 3.0.3 on 2021-07-07 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0014_auto_20210705_0738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='status',
        ),
    ]
