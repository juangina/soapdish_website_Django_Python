# Generated by Django 3.2.5 on 2021-10-15 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_inventory_bar_soap'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='purchase_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]