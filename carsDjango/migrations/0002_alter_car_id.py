# Generated by Django 4.1.7 on 2023-02-20 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsDjango', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]