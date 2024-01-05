# Generated by Django 4.2.7 on 2023-12-28 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre del plato')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Precio')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('categories', models.ManyToManyField(related_name='get_posts', to='categos.category', verbose_name='Categorías')),
            ],
            options={
                'verbose_name': 'plato',
                'verbose_name_plural': 'platos',
                'ordering': ['created'],
            },
        ),
    ]
