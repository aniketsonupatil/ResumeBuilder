# Generated by Django 3.2.4 on 2021-06-22 05:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AchivementTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type_Achive', models.CharField(help_text='Enter Achivement Type', max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Make must be greater than 1 character')])),
            ],
        ),
        migrations.CreateModel(
            name='Achivement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AchivementName', models.CharField(help_text='Enter Achivement', max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Make must be greater than 1 character')])),
                ('AchivementPeriod', models.CharField(help_text='Enter Achivement Time Period', max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Make must be greater than 1 character')])),
                ('AchiveType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ResBuild.achivementtypes')),
            ],
        ),
    ]
