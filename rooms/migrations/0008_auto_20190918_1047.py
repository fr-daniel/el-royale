# Generated by Django 2.2.5 on 2019-09-18 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0004_auto_20190918_0933'),
        ('rooms', '0007_auto_20190918_0942'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='room',
            unique_together={('number', 'hotel')},
        ),
    ]
