# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 18:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ophasebase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutor_name', models.CharField(max_length=100, verbose_name='Name')),
                ('tutor_mail', models.EmailField(max_length=254, verbose_name='E-Mail-Adresse')),
                ('title', models.CharField(help_text='Unter welcher Überschrift steht der Workshop?', max_length=200, verbose_name='Workshoptitel')),
                ('workshop_type', models.CharField(help_text='Welche Art Veranstaltung ist das? Vortrag, Vortrag mit Hands-on, Workshop, Sport, Ausflug, ...', max_length=40, verbose_name='Art des Workshops')),
                ('how_often', models.PositiveSmallIntegerField(help_text='Wie oft kann dieser Workshop angeboten werden?', verbose_name='Anzahl')),
                ('location_info', models.CharField(help_text='Wo soll der Workshop stattfinden (Hörsaal, Gruppenraum, Poolraum, ...)?', max_length=200, verbose_name='Raumbedarf')),
                ('max_participants', models.PositiveSmallIntegerField(help_text='Maximale Teilnehmeranzahl (auf 0 lassen für volle Raumkapazität).', verbose_name='Max. Teilnehmerzahl')),
                ('equipment', models.CharField(blank=True, help_text='Wird etwas benötigt das wir zur Verfügung stellen sollen?', max_length=200, verbose_name='Benötigtes Material')),
                ('participant_requirements', models.TextField(blank=True, help_text='Benötigen die Teilnehmer Vorkenntnisse oder müssen sie etwas mitbringen?', verbose_name='Teilnahmevoraussetzungen')),
                ('description', models.TextField(help_text='Eine kurze Beschreibung um was es geht und was die Teilnehmer erwartet.', verbose_name='Beschreibungstext')),
                ('remarks', models.TextField(blank=True, help_text='Sonstige Informationen', verbose_name='Anmerkungen')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ophase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ophasebase.Ophase')),
            ],
            options={
                'verbose_name_plural': 'Workshops',
                'verbose_name': 'Workshop',
            },
        ),
        migrations.CreateModel(
            name='WorkshopSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Datum')),
                ('start_time', models.TimeField(verbose_name='Beginn')),
                ('end_time', models.TimeField(verbose_name='Ende')),
                ('ophase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ophasebase.Ophase')),
            ],
            options={
                'verbose_name_plural': 'Workshopslots',
                'verbose_name': 'Workshopslot',
                'ordering': ['date', 'start_time'],
            },
        ),
        migrations.AddField(
            model_name='workshop',
            name='possible_slots',
            field=models.ManyToManyField(help_text='Welche Slots sind zeitlich möglich (unabhängig davon wie oft der Workshop stattfinden kann)?', to='workshops.WorkshopSlot', verbose_name='Mögliche Zeitslots'),
        ),
    ]
