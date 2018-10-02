# Generated by Django 2.0.6 on 2018-10-02 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20181002_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='degree',
            name='degree_diploma',
            field=models.CharField(choices=[('Bachelor', 'Bachelor of Science'), ('Master', 'Master of Science'), ('PhD', 'Doctor of Science')], default='Bachelor of Science', max_length=50),
        ),
    ]