# Generated by Django 4.2 on 2023-06-07 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactform', '0003_auto_20230607_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmodel',
            name='subject',
            field=models.CharField(default='Default Subject', max_length=100),
        ),
    ]
