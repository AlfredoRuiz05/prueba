# Generated by Django 5.0.6 on 2024-08-07 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_favorito'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='activo',
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
