# Generated by Django 5.1.4 on 2024-12-20 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField()),
                ('fname', models.CharField(max_length=80)),
                ('lname', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=80)),
            ],
        ),
    ]
