# Generated by Django 3.0.5 on 2022-04-27 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20220427_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subj',
            name='prof_art',
            field=models.PositiveIntegerField(blank=True, default='0'),
        ),
        migrations.AlterField(
            model_name='subj',
            name='prof_conventional',
            field=models.PositiveIntegerField(blank=True, default='0'),
        ),
        migrations.AlterField(
            model_name='subj',
            name='prof_initiative',
            field=models.PositiveIntegerField(blank=True, default='0'),
        ),
        migrations.AlterField(
            model_name='subj',
            name='prof_intellect',
            field=models.PositiveIntegerField(blank=True, default='0'),
        ),
        migrations.AlterField(
            model_name='subj',
            name='prof_real',
            field=models.PositiveIntegerField(blank=True, default='0'),
        ),
        migrations.AlterField(
            model_name='subj',
            name='prof_social',
            field=models.PositiveIntegerField(blank=True, default='0'),
        ),
    ]
