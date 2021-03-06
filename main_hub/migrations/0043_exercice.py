# Generated by Django 2.2.5 on 2020-02-07 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_hub', '0042_support'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sujet', models.FileField(upload_to='uploads/trainingmath/sujets/')),
                ('correction', models.FileField(upload_to='uploads/trainingmath/corrections/')),
                ('chapitres', models.TextField()),
                ('points', models.CharField(max_length=10)),
                ('difficulte', models.CharField(max_length=30)),
            ],
        ),
    ]
