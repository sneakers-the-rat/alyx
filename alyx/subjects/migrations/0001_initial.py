# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-06 09:07
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('equipment', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Allele',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Structured data, formatted in a user-defined way', null=True)),
                ('standard_name', models.CharField(help_text='MGNC-standard genotype name e.g. Pvalb<tm1(cre)Arbr>, http://www.informatics.jax.org/mgihome/nomen/', max_length=1023)),
                ('informal_name', models.CharField(help_text='informal name in lab, e.g. Pvalb-Cre', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Structured data, formatted in a user-defined way', null=True)),
                ('cage_label', models.CharField(default='-', help_text='Leave to "-" to autofill.', max_length=255)),
                ('type', models.CharField(choices=[('I', 'IVC'), ('R', 'Regular')], default='I', help_text='Is this an IVC or regular cage?', max_length=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GenotypeTest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Structured data, formatted in a user-defined way', null=True)),
                ('test_result', models.IntegerField(choices=[(0, 'Absent'), (1, 'Present')])),
            ],
            options={
                'verbose_name_plural': 'genotype tests',
            },
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Structured data, formatted in a user-defined way', null=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('target_phenotype', models.CharField(max_length=1023)),
                ('auto_name', models.SlugField(max_length=255)),
                ('subject_autoname_index', models.IntegerField(default=0)),
                ('cage_autoname_index', models.IntegerField(default=0)),
                ('litter_autoname_index', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Litter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Structured data, formatted in a user-defined way', null=True)),
                ('descriptive_name', models.CharField(default='-', max_length=255)),
                ('notes', models.TextField(blank=True, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('cage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subjects.Cage')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Structured data, formatted in a user-defined way', null=True)),
                ('base_pairs', models.TextField(help_text='the actual sequence of base pairs in the test')),
                ('description', models.CharField(help_text='any other relevant information about this test', max_length=1023)),
                ('informal_name', models.CharField(help_text='informal name in lab, e.g. ROSA-WT', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Structured data, formatted in a user-defined way', null=True)),
                ('name', models.CharField(max_length=255)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Structured data, formatted in a user-defined way', null=True)),
                ('binomial', models.CharField(help_text='Binomial name, e.g. "mus musculus"', max_length=255)),
                ('display_name', models.CharField(help_text='common name, e.g. "mouse"', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'species',
            },
        ),
        migrations.CreateModel(
            name='Strain',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Structured data, formatted in a user-defined way', null=True)),
                ('descriptive_name', models.CharField(help_text='Standard descriptive name E.g. "C57BL/6J", http://www.informatics.jax.org/mgihome/nomen/', max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Structured data, formatted in a user-defined way', null=True)),
                ('nickname', models.SlugField(allow_unicode=True, default='-', help_text="Easy-to-remember, unique name (e.g. 'Hercules').", max_length=255, unique=True)),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unknown')], default='U', max_length=1, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('death_date', models.DateField(blank=True, null=True)),
                ('wean_date', models.DateField(blank=True, null=True)),
                ('implant_weight', models.FloatField(blank=True, help_text='Implant weight in grams', null=True)),
                ('ear_mark', models.CharField(blank=True, max_length=32, null=True)),
                ('protocol_number', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='3', max_length=1)),
                ('notes', models.TextField(blank=True, null=True)),
                ('cull_method', models.TextField(blank=True, null=True)),
                ('adverse_effects', models.TextField(blank=True, null=True)),
                ('actual_severity', models.CharField(blank=True, choices=[('st', 'Sub-threshold'), ('mi', 'Mild'), ('mo', 'Moderate'), ('se', 'Severe'), ('nr', 'Non-recovery')], max_length=2, null=True)),
                ('cage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subjects.Cage')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubjectRequest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Structured data, formatted in a user-defined way', null=True)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('date_time', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('line', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subjects.Line')),
                ('user', models.ForeignKey(blank=True, help_text='Who requested this subject.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subjects_requested', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Zygosity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Structured data, formatted in a user-defined way', null=True)),
                ('zygosity', models.IntegerField(choices=[(0, 'Absent'), (1, 'Heterozygous'), (2, 'Homozygous'), (3, 'Present')])),
                ('allele', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.Allele')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.Subject')),
            ],
            options={
                'verbose_name_plural': 'zygosities',
            },
        ),
        migrations.AddField(
            model_name='subject',
            name='genotype',
            field=models.ManyToManyField(through='subjects.Zygosity', to='subjects.Allele'),
        ),
        migrations.AddField(
            model_name='subject',
            name='genotype_test',
            field=models.ManyToManyField(through='subjects.GenotypeTest', to='subjects.Sequence'),
        ),
        migrations.AddField(
            model_name='subject',
            name='line',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subjects.Line'),
        ),
        migrations.AddField(
            model_name='subject',
            name='litter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subjects.Litter'),
        ),
        migrations.AddField(
            model_name='subject',
            name='request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subjects.SubjectRequest'),
        ),
        migrations.AddField(
            model_name='subject',
            name='responsible_user',
            field=models.ForeignKey(blank=True, help_text='Who has primary or legal responsibility for the subject.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subjects_responsible', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='subject',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subjects.Source'),
        ),
        migrations.AddField(
            model_name='subject',
            name='species',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subjects.Species'),
        ),
        migrations.AddField(
            model_name='subject',
            name='strain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subjects.Strain'),
        ),
        migrations.AddField(
            model_name='litter',
            name='father',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='litter_father', to='subjects.Subject'),
        ),
        migrations.AddField(
            model_name='litter',
            name='line',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subjects.Line'),
        ),
        migrations.AddField(
            model_name='litter',
            name='mother',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='litter_mother', to='subjects.Subject'),
        ),
        migrations.AddField(
            model_name='line',
            name='sequences',
            field=models.ManyToManyField(to='subjects.Sequence'),
        ),
        migrations.AddField(
            model_name='line',
            name='species',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subjects.Species'),
        ),
        migrations.AddField(
            model_name='line',
            name='strain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subjects.Strain'),
        ),
        migrations.AddField(
            model_name='genotypetest',
            name='sequence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.Sequence'),
        ),
        migrations.AddField(
            model_name='genotypetest',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.Subject'),
        ),
        migrations.AddField(
            model_name='cage',
            name='line',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subjects.Line'),
        ),
        migrations.AddField(
            model_name='cage',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.LabLocation'),
        ),
        migrations.CreateModel(
            name='Subjects - adverse effect',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('subjects.subject',),
        ),
        migrations.AlterField(
            model_name='line',
            name='auto_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='subject',
            name='nickname',
            field=models.CharField(default='-', help_text="Easy-to-remember, unique name (e.g. 'Hercules').", max_length=255, unique=True),
        ),
    ]
