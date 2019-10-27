# Generated by Django 2.2.6 on 2019-10-27 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tp_acp1', '0010_categoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='activa',
            new_name='activo',
        ),
        migrations.AddField(
            model_name='plato',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='tp_acp1.Categoria'),
        ),
    ]
