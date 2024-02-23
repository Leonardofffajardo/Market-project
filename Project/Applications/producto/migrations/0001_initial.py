# Generated by Django 3.0.6 on 2024-02-09 21:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100, verbose_name='Razon Social')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=40, verbose_name='telefonos')),
                ('web', models.URLField(blank=True, verbose_name='sitio web')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('barcode', models.CharField(max_length=13, unique=True)),
                ('name', models.CharField(max_length=40, verbose_name='Nombre')),
                ('due_date', models.DateField(blank=True, null=True, verbose_name='fehca de vencimiento')),
                ('description', models.TextField(blank=True, verbose_name='descripcion del producto')),
                ('unit', models.CharField(choices=[('0', 'Kilogramos'), ('1', 'Litros'), ('2', 'Unidades')], max_length=1, verbose_name='unidad de medida')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='cantidad en almacen')),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='precio compra')),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='precio venta')),
                ('num_sale', models.PositiveIntegerField(default=0, verbose_name='numero de ventas')),
                ('anulate', models.BooleanField(default=False, verbose_name='eliminado')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.Marca')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.Provider')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
