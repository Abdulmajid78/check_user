# Generated by Django 4.2.5 on 2023-11-09 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companymodel',
            name='established',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
