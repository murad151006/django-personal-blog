# Generated by Django 3.0.6 on 2020-06-13 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('slno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('posted', models.DateTimeField(blank=True)),
            ],
        ),
    ]