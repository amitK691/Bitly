# Generated by Django 3.2.4 on 2021-06-07 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crul', '0002_rename_url_container_linkcontainer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='linkcontainer',
            old_name='login_url',
            new_name='long_url',
        ),
    ]
