# Generated by Django 5.0.2 on 2024-03-11 02:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='cliente',
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=100)),
                ('documento', models.CharField(max_length=20, unique=True)),
                ('cantidad', models.IntegerField()),
                ('monto_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.producto')),
            ],
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Venta',
        ),
    ]