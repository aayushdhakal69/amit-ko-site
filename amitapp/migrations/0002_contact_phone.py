# Generated by Django 4.1.7 on 2023-07-07 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amitapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default=1234567890, max_length=15),
            preserve_default=False,
        ),
    ]