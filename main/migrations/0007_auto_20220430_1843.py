# Generated by Django 3.0.5 on 2022-04-30 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20220430_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sphere',
            name='title',
            field=models.CharField(blank=True, max_length=200, verbose_name='title'),
        ),
    ]