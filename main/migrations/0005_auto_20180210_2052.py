# Generated by Django 2.0.2 on 2018-02-10 20:52

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180210_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuesta',
            name='price',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('11', 'bueno'), ('12', 'malo')], default=' ', max_length=5),
        ),
    ]