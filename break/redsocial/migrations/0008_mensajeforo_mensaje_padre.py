# Generated by Django 5.0.4 on 2024-07-06 05:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redsocial', '0007_remove_usuario_activo_remove_usuario_direccion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensajeforo',
            name='mensaje_padre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='respuestas', to='redsocial.mensajeforo'),
        ),
    ]
