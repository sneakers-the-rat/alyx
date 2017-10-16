# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-08 14:04
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('actions', '0002_experiment'),
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataCollection',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Structured data, formatted in a user-defined way', null=True)),
                ('created_datetime', models.DateTimeField(blank=True, default=django.utils.timezone.now, help_text='The creation datetime.', null=True)),
                ('generating_software', models.CharField(blank=True, help_text="e.g. 'ChoiceWorld 0.8.3'", max_length=255)),
                ('name', models.CharField(blank=True, help_text='description of the data in this collection (e.g. cluster information)', max_length=255)),
                ('created_by', models.ForeignKey(blank=True, help_text='The creator of the data.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='data_datacollection_created_by_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='eventseries',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='eventseries',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='eventseries',
            name='description',
        ),
        migrations.RemoveField(
            model_name='eventseries',
            name='event_times',
        ),
        migrations.RemoveField(
            model_name='eventseries',
            name='event_types',
        ),
        migrations.RemoveField(
            model_name='eventseries',
            name='generating_software',
        ),
        migrations.RemoveField(
            model_name='eventseries',
            name='id',
        ),
        migrations.RemoveField(
            model_name='eventseries',
            name='json',
        ),
        migrations.RemoveField(
            model_name='eventseries',
            name='provenance_directory',
        ),
        migrations.RemoveField(
            model_name='eventseries',
            name='session',
        ),
        migrations.RemoveField(
            model_name='eventseries',
            name='type_descriptions',
        ),
        migrations.RemoveField(
            model_name='intervalseries',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='intervalseries',
            name='description',
        ),
        migrations.RemoveField(
            model_name='intervalseries',
            name='interval_times',
        ),
        migrations.RemoveField(
            model_name='intervalseries',
            name='interval_types',
        ),
        migrations.RemoveField(
            model_name='intervalseries',
            name='type_descriptions',
        ),
        migrations.RemoveField(
            model_name='timescale',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='timescale',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='timescale',
            name='session',
        ),
        migrations.RemoveField(
            model_name='timeseries',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='timeseries',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='timeseries',
            name='data',
        ),
        migrations.RemoveField(
            model_name='timeseries',
            name='id',
        ),
        migrations.RemoveField(
            model_name='timeseries',
            name='json',
        ),
        migrations.RemoveField(
            model_name='timeseries',
            name='session',
        ),
        migrations.AddField(
            model_name='dataset',
            name='created_datetime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, help_text='The creation datetime.', null=True),
        ),
        migrations.AddField(
            model_name='dataset',
            name='experiment',
            field=models.ForeignKey(blank=True, help_text='The Experiment to which this data belongs', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='data_dataset_session_related', to='actions.Experiment'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='generating_software',
            field=models.CharField(blank=True, help_text="e.g. 'ChoiceWorld 0.8.3'", max_length=255),
        ),
        migrations.AddField(
            model_name='dataset',
            name='provenance_directory',
            field=models.ForeignKey(blank=True, help_text='link to directory containing intermediate results', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='data_dataset_provenance_related', to='data.Dataset'),
        ),
        migrations.AddField(
            model_name='eventseries',
            name='times',
            field=models.ForeignKey(blank=True, help_text='n*1 array of times on specified timescale', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='data_eventseries_event_times_related', to='data.Dataset'),
        ),
        migrations.AddField(
            model_name='intervalseries',
            name='created_datetime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, help_text='The creation datetime.', null=True),
        ),
        migrations.AddField(
            model_name='intervalseries',
            name='experiment',
            field=models.ForeignKey(blank=True, help_text='The Experiment to which this data belongs', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='data_intervalseries_session_related', to='actions.Experiment'),
        ),
        migrations.AddField(
            model_name='intervalseries',
            name='intervals',
            field=models.ForeignKey(blank=True, help_text='n*2 array of start and end times', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='data_intervalseries_interval_times_related', to='data.Dataset'),
        ),
        migrations.AlterField(
            model_name='datarepository',
            name='path',
            field=models.CharField(blank=True, help_text='absolute URI path to the repository', max_length=1000),
        ),
        migrations.AlterField(
            model_name='intervalseries',
            name='provenance_directory',
            field=models.ForeignKey(blank=True, help_text='link to directory containing intermediate results', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='data_intervalseries_provenance_related', to='data.Dataset'),
        ),
        migrations.AlterField(
            model_name='timeseries',
            name='timescale',
            field=models.ForeignKey(blank=True, help_text='which timescale this is on', null=True, on_delete=django.db.models.deletion.CASCADE, to='data.Timescale'),
        ),
        migrations.AlterField(
            model_name='timeseries',
            name='timestamps',
            field=models.ForeignKey(blank=True, help_text='N*2 array containing sample numbers and their timestamps on associated timescale', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='data_timeseries_timestamps_related', to='data.Dataset'),
        ),
        migrations.AddField(
            model_name='datacollection',
            name='data',
            field=models.ManyToManyField(blank=True, help_text='Datasets, each of which  should have their own descriptions and DatasetTypes', related_name='data_datacollection_data_related', to='data.Dataset'),
        ),
        migrations.AddField(
            model_name='datacollection',
            name='experiment',
            field=models.ForeignKey(blank=True, help_text='The Experiment to which this data belongs', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='data_datacollection_session_related', to='actions.Experiment'),
        ),
        migrations.AddField(
            model_name='datacollection',
            name='provenance_directory',
            field=models.ForeignKey(blank=True, help_text='link to directory containing intermediate results', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='data_datacollection_provenance_related', to='data.Dataset'),
        ),
        migrations.AddField(
            model_name='datacollection',
            name='session',
            field=models.ForeignKey(blank=True, help_text='The Session to which this data belongs', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='data_datacollection_session_related', to='actions.Session'),
        ),
        migrations.AddField(
            model_name='eventseries',
            name='datacollection_ptr',
            field=models.OneToOneField(auto_created=True, default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='data.DataCollection'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timeseries',
            name='datacollection_ptr',
            field=models.OneToOneField(auto_created=True, default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='data.DataCollection'),
            preserve_default=False,
        ),
    ]