# Generated by Django 4.2.2 on 2023-07-28 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0009_rename_profile_model_userprofile_model'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile_model',
            options={'verbose_name_plural': 'User Profile'},
        ),
    ]
