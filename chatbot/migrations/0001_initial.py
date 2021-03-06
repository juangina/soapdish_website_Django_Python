# Generated by Django 3.2.5 on 2021-09-06 17:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation_Meta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('dialog_started', models.BooleanField(blank=True, default=False, null=True)),
                ('dialog_completed', models.BooleanField(blank=True, default=False, null=True)),
                ('temp_data', models.CharField(default='', max_length=100)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Conversation_Dialog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dialog', models.CharField(max_length=200)),
                ('intent', models.CharField(default='None', max_length=100)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('conversation_meta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatbot.conversation_meta')),
            ],
        ),
    ]
