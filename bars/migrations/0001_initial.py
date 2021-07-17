# Generated by Django 3.2.5 on 2021-07-17 02:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('creators', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('recipe', models.CharField(default='Brambleberry', max_length=100)),
                ('fragrance', models.CharField(default='Sans', max_length=100)),
                ('batch_code', models.CharField(max_length=100)),
                ('colorants', models.TextField(blank=True, max_length=200)),
                ('nutrients', models.TextField(blank=True, max_length=200)),
                ('exfolients', models.TextField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('price', models.IntegerField(default=5)),
                ('discount', models.IntegerField(default=8)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_cured', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='creators.creator')),
            ],
        ),
    ]
