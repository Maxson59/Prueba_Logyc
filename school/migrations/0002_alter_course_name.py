# Generated by Django 4.2.2 on 2023-06-13 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]