# Generated by Django 3.0.8 on 2020-07-18 12:53

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
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('level_code', models.CharField(max_length=5)),
                ('alias', models.CharField(max_length=10)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingapp.Building')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('booking_type', models.CharField(choices=[('meeting', 'For a meeting'), ('event', 'For an event')], default=('meeting', 'For a meeting'), max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('link', models.URLField()),
                ('book_start_date', models.DateField()),
                ('book_end_date', models.DateField()),
                ('book_start_time', models.TimeField()),
                ('book_end_time', models.TimeField()),
                ('what_to_bring', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookingapp.Level')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
