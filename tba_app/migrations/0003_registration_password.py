# Generated by Django 3.0 on 2020-02-03 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tba_app', '0002_auto_20200203_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='password',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
