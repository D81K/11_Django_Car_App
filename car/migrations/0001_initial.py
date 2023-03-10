# Generated by Django 3.2.16 on 2023-01-11 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate_number', models.CharField(max_length=15, unique=True)),
                ('brand', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=50)),
                ('year', models.SmallIntegerField()),
                ('gaer', models.CharField(choices=[('a', 'Automatic'), ('m', 'Manuel')], max_length=1)),
                ('rent_per_day', models.IntegerField()),
                ('availability', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.car')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='reservation',
            constraint=models.UniqueConstraint(fields=('customer', 'start_date', 'end_date'), name='user_rent_dates'),
        ),
    ]
