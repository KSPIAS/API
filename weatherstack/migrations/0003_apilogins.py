# Generated by Django 5.1 on 2024-08-17 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherstack', '0002_apilogin_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='apilogins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('pwd', models.CharField(max_length=100)),
            ],
        ),
    ]