# Generated by Django 5.0.4 on 2024-07-06 02:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id_genero', models.AutoField(db_column='idgenero', primary_key=True, serialize=False)),
                ('genero', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('isbn', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=50)),
                ('editorial', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rol', models.AutoField(db_column='idrol', primary_key=True, serialize=False)),
                ('rol', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CompraLibro',
            fields=[
                ('id_compra', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.PositiveIntegerField()),
                ('fecha_compra', models.DateField(auto_now_add=True)),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redsocial.libro')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido_paterno', models.CharField(max_length=20)),
                ('apellido_materno', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=45)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('id_genero', models.ForeignKey(db_column='idgenero', on_delete=django.db.models.deletion.CASCADE, to='redsocial.genero')),
                ('id_rol', models.ForeignKey(db_column='idrol', on_delete=django.db.models.deletion.CASCADE, to='redsocial.rol')),
            ],
        ),
        migrations.CreateModel(
            name='MensajeForo',
            fields=[
                ('id_mensaje', models.AutoField(primary_key=True, serialize=False)),
                ('contenido', models.TextField()),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redsocial.usuario')),
            ],
        ),
    ]