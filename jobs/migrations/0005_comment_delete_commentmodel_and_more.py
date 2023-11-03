# Generated by Django 4.2.5 on 2023-11-03 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_alter_commentmodel_employ_to'),
    ]

    operations = [
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
            },
        ),
        migrations.DeleteModel(
            name='CommentModel',
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['created_at'], name='jobs_commen_created_c341ee_idx'),
        ),
    ]