# Generated by Django 3.2.5 on 2023-05-13 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20220127_0904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='listing',
            new_name='bar',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='listing_id',
            new_name='bar_id',
        ),
    ]
