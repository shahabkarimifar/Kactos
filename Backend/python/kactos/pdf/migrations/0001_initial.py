# Generated by Django 3.0.3 on 2020-03-06 06:46

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
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('father_id', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='covers/')),
                ('summary', models.TextField()),
                ('stars', models.IntegerField(default=0)),
                ('file', models.FileField(upload_to='pdfs/')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdf.Genre')),
                ('uploader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]