# Generated by Django 2.2.6 on 2019-10-27 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tp_acp1', '0009_sugerencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('activa', models.BooleanField()),
            ],
        ),
    ]
