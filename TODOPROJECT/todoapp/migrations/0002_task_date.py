# Generated by Django 4.2.1 on 2023-05-08 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2023-05-09'),
            preserve_default=False,
        ),
    ]
