# Generated by Django 4.1 on 2022-08-19 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='place',
            field=models.TextField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
