# Generated by Django 2.2.3 on 2019-08-12 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_hub', '0014_auto_20190810_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='vekflix',
            name='categorie',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
