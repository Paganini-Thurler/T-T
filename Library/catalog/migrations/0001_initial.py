# Generated by Django 5.0.6 on 2024-06-20 18:06

import django.db.models.deletion
import django.db.models.functions.text
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('death_date', models.DateField(blank=True, null=True, verbose_name='Deceassed')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Book's genre, for example: Historic Fiction, Horror.", max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(help_text="Book's description", max_length=1000)),
                ('isbn', models.CharField(help_text="Book's ISBN number", max_length=13, unique=True, verbose_name='ISBN')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalog.author')),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text="Book's unique identifier", primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200)),
                ('reservation_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('a', 'Available'), ('m', 'Maintencenance'), ('o', 'On loan'), ('r', 'Reserved')], default='a', help_text='Book availability', max_length=1)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalog.book')),
            ],
            options={
                'ordering': ['reservation_date'],
            },
        ),
        migrations.AddConstraint(
            model_name='genre',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='genere_name_case_insensitive_unique', violation_error_message='Genre exits'),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text="Book's genre", to='catalog.genre'),
        ),
    ]
