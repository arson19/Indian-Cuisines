# Generated by Django 3.1.7 on 2022-07-08 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='cook_time',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='foods',
            name='prep_time',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]