# Generated by Django 4.0.4 on 2022-06-28 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0004_rename_contactforjoin_contactforjoindb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactforjoindb',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
