# Generated by Django 4.0.4 on 2023-11-08 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_registeredevents'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeredevents',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
    ]
