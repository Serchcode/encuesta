# Generated by Django 2.0.2 on 2018-02-10 20:22

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180210_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encuesta',
            name='price_bad',
        ),
        migrations.RemoveField(
            model_name='encuesta',
            name='price_god',
        ),
        migrations.AddField(
            model_name='encuesta',
            name='price',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('11', 'malo'), ('12', 'bueno')], default=' ', max_length=5),
        ),
    ]