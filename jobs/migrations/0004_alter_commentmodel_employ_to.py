# Generated by Django 4.2.5 on 2023-11-02 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_employeemodel_born_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='employ_to',
            field=models.DateField(),
        ),
    ]