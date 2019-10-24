# Generated by Django 2.2.6 on 2019-10-24 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tp_acp1', '0003_auto_20191024_0349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.CharField(max_length=30)),
                ('imagen', models.ImageField(upload_to='imagenes/plato')),
                ('descripcion', models.CharField(max_length=400)),
                ('activo', models.BooleanField()),
            ],
        ),
    ]
