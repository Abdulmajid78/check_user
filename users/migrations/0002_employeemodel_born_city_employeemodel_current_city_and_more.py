# Generated by Django 4.2.5 on 2023-10-12 13:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemodel',
            name='born_city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='current_city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='is_applicant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='is_employer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, null=True),
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='third_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]