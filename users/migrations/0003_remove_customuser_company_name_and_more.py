# Generated by Django 4.2.5 on 2023-10-24 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_company_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='company_name',
        ),
        migrations.AddField(
            model_name='companyuser',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
