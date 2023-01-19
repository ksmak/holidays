# Generated by Django 4.1.5 on 2023-01-18 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionaries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='наименование')),
            ],
            options={
                'verbose_name': ('звание',),
                'verbose_name_plural': 'звания',
                'ordering': ('title',),
            },
        ),
    ]