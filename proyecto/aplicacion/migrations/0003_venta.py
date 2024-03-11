# Generated by Django 5.0.2 on 2024-03-11 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_remove_venta_cliente_proveedor_delete_cliente_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=100)),
                ('documento', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=50)),
                ('precio_venta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
            ],
        ),
    ]