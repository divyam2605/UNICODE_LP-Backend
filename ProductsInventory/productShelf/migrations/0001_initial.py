# Generated by Django 4.0.4 on 2022-11-11 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('productname', models.CharField(max_length=30)),
                ('companyname', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('stock_left', models.IntegerField()),
            ],
        ),
    ]
