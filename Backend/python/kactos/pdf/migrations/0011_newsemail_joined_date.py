# Generated by Django 3.0.3 on 2020-03-09 10:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0010_auto_20200309_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsemail',
            name='joined_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
