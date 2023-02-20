# Generated by Django 4.1.7 on 2023-02-20 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=200)),
                ('carModel', models.CharField(max_length=200)),
                ('yearOfConstruct', models.DateField()),
                ('cylindre', models.IntegerField(default=0)),
                ('version', models.CharField(max_length=200)),
            ],
        ),
    ]
