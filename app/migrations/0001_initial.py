# Generated by Django 3.2 on 2021-05-01 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=130)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('job_title', models.CharField(blank=True, max_length=30)),
                ('bio', models.TextField(blank=True)),
                ('age', models.IntegerField(blank=True)),
            ],
        ),
    ]
