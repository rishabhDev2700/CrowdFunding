# Generated by Django 4.0.5 on 2022-07-15 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_userprofile_bio_userprofile_loaction_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='loaction',
            new_name='location',
        ),
    ]