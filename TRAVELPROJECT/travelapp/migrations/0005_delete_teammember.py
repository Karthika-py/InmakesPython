# Generated by Django 4.1.7 on 2023-04-14 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0004_rename_desc_teammember_teamdesc_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TeamMember',
        ),
    ]
