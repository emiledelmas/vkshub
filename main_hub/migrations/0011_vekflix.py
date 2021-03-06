# Generated by Django 2.2.3 on 2019-08-08 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_hub', '0010_projet_site'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vekflix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('simple_description', models.CharField(max_length=20)),
                ('film', models.FileField(upload_to='vekflix/film/')),
                ('realisator', models.CharField(max_length=20)),
                ('main_actor', models.CharField(max_length=20)),
                ('jacket', models.ImageField(blank=True, null=True, upload_to='vekflix/image/')),
                ('mignature', models.ImageField(blank=True, null=True, upload_to='vekflix/image/')),
            ],
        ),
    ]
