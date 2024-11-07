# Generated by Django 5.0.1 on 2024-11-07 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('serialNumber', models.CharField(max_length=10)),
                ('price', models.FloatField()),
            ],
        ),
    ]
