# Generated by Django 4.1.2 on 2023-05-31 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_usuarios_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='activo',
            field=models.IntegerField(default=1),
        ),
    ]
