# Generated by Django 4.2.2 on 2023-06-13 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_alter_teacher_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='Course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.course'),
        ),
    ]
