# Generated by Django 4.0 on 2023-08-20 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0005_alter_job_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
