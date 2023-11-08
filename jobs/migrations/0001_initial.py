# Generated by Django 4.2.5 on 2023-11-05 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Shahar',
                'verbose_name_plural': 'Shaharlar',
            },
        ),
        migrations.CreateModel(
            name='ExperienceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=49)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Tajriba',
                'verbose_name_plural': 'Tajribalar',
            },
        ),
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('third_name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=17, null=True)),
                ('born_date', models.DateField()),
                ('about', models.TextField(blank=True, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_applicant', models.BooleanField(default=False)),
                ('is_employer', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('born_city', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='born_city', to='jobs.citymodel')),
                ('current_city', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='current_city', to='jobs.citymodel')),
                ('experience', models.ManyToManyField(blank=True, null=True, related_name='experience', to='jobs.experiencemodel')),
            ],
            options={
                'verbose_name': 'Ishchi',
                'verbose_name_plural': 'Ishchilar',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('position', models.CharField(max_length=60)),
                ('employ_from', models.DateField()),
                ('employ_to', models.DateField()),
                ('content', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='jobs.employeemodel')),
            ],
            options={
                'verbose_name': 'Ish tajriba',
                'verbose_name_plural': 'Ish tajribalar',
                'ordering': ['created_at'],
                'indexes': [models.Index(fields=['created_at'], name='jobs_commen_created_c341ee_idx')],
            },
        ),
    ]
