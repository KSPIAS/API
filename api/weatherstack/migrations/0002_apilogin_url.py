# Generated by Django 5.1 on 2024-08-17 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherstack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apilogin',
            name='url',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
