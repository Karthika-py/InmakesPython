# Generated by Django 4.1.7 on 2023-04-14 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_teammembers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TeamMembers',
            new_name='TeamMember',
        ),
    ]
