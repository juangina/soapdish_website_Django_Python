# Generated by Django 3.2.5 on 2021-12-20 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20210731_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
