# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-22 14:06
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subjects', '0002_auto_20160422_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('narrative', models.TextField(blank=True, null=True)),
                ('start_date_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('end_date_time', models.DateTimeField(blank=True, null=True)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, null=True, size=30)),
                ('JSON', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Virus_Batch',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('virus_type', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('virus_source', models.CharField(blank=True, max_length=255, null=True)),
                ('date_time_made', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('nominal_titer', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('action_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actions.Action')),
            ],
            bases=('actions.action',),
        ),
        migrations.CreateModel(
            name='Surgery',
            fields=[
                ('action_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actions.Action')),
                ('procedure', models.CharField(blank=True, max_length=255, null=True)),
                ('brain_location', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'surgeries',
            },
            bases=('actions.action',),
        ),
        migrations.CreateModel(
            name='Virus_Injection',
            fields=[
                ('action_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actions.Action')),
                ('injection_volume', models.FloatField(blank=True, null=True)),
                ('rate_of_injection', models.FloatField(blank=True, null=True)),
                ('injection_type', models.CharField(blank=True, choices=[('I', 'Iontophoresis'), ('P', 'Pressure')], default='I', max_length=1, null=True)),
                ('virus_batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actions.Virus_Batch')),
            ],
            bases=('actions.action',),
        ),
        migrations.CreateModel(
            name='Weighing',
            fields=[
                ('action_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actions.Action')),
                ('weight', models.FloatField()),
            ],
            bases=('actions.action',),
        ),
        migrations.AddField(
            model_name='action',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='subjects.Subject'),
        ),
        migrations.AddField(
            model_name='action',
            name='users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
