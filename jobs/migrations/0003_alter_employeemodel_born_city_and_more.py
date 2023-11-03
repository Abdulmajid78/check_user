# Generated by Django 4.2.5 on 2023-11-02 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='born_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='born_city', to='jobs.citymodel'),
        ),
        migrations.AlterField(
            model_name='employeemodel',
            name='current_city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, related_name='current_city', to='jobs.citymodel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employeemodel',
            name='experience',
            field=models.ManyToManyField(blank=True, null=True, related_name='experience', to='jobs.experiencemodel'),
        ),
    ]