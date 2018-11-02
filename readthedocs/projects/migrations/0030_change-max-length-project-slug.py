# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-01 20:55
from __future__ import unicode_literals

from django.db import migrations, models
from django.db.models.functions import Length


def forwards_func(apps, schema_editor):
    max_length = 63
    Project = apps.get_model('projects', 'Project')
    projects_invalid_slug = (
        Project
        .objects
        .annotate(slug_length=Length('slug'))
        .filter(slug_length__gt=max_length)
    )
    for project in projects_invalid_slug:
        project.slug = project.slug[:max_length]
        project.save()

    projects_invalid_name = (
        Project
        .objects
        .annotate(name_length=Length('name'))
        .filter(name_length__gt=max_length)
    )
    for project in projects_invalid_name:
        project.name = project.name[:max_length]
        project.save()


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0029_add_additional_languages'),
    ]

    operations = [
        migrations.RunPython(forwards_func),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(max_length=63, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=63, verbose_name='Name'),
        ),
    ]
