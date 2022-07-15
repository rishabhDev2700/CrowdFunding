# Generated by Django 4.0.5 on 2022-07-15 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_userprofile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='loaction',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='occupation',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='contact',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
