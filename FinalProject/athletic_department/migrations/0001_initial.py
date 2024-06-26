# Generated by Django 5.0.1 on 2024-04-08 23:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sport_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('income', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('expense', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='athletic_department.team')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='athletic_department.team')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='athletic_department.team')),
            ],
        ),
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('scholarship_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='athletic_department.team')),
            ],
        ),
    ]
