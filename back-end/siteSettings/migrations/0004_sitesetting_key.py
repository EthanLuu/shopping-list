# Generated by Django 3.2.9 on 2021-12-25 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteSettings', '0003_alter_sitesetting_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='key',
            field=models.CharField(default='', max_length=20),
        ),
    ]
