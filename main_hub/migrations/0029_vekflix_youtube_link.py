# Generated by Django 2.2.5 on 2019-10-12 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_hub', '0028_auto_20190925_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='vekflix',
            name='youtube_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
