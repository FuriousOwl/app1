# Generated by Django 4.2.7 on 2024-05-26 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='category',
        ),
    ]
