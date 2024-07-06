# Generated by Django 5.0.4 on 2024-07-06 04:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redsocial', '0004_alter_usuario_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id_genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redsocial.genero'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id_rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redsocial.rol'),
        ),
        migrations.AlterModelTable(
            name='usuario',
            table='usuario',
        ),
    ]
