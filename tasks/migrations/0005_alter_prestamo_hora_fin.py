# Generated by Django 3.2.8 on 2024-02-27 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_prestamo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='hora_fin',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
