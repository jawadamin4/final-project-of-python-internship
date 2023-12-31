# Generated by Django 4.2.3 on 2023-07-26 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('last_price', models.CharField(max_length=20)),
                ('change', models.CharField(max_length=20)),
                ('percentage_change', models.CharField(max_length=20)),
            ],
        ),
    ]
