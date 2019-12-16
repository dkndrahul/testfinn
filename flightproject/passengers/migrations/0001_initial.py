# Generated by Django 2.1 on 2019-12-15 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlightsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flightNumber', models.CharField(max_length=30)),
                ('departureAirport', models.CharField(max_length=3)),
                ('arrivalAirport', models.CharField(max_length=3)),
                ('departureDate', models.DateField()),
                ('arrivalDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PassengersModel',
            fields=[
                ('passengerId', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('bookingId', models.CharField(max_length=6)),
                ('email', models.CharField(max_length=30)),
                ('flights', models.ManyToManyField(to='passengers.FlightsModel')),
            ],
        ),
    ]
