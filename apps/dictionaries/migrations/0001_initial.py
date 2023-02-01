# Generated by Django 4.1.5 on 2023-02-01 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('abstracts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('abstractdictionary_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='abstracts.abstractdictionary')),
            ],
            options={
                'verbose_name': ('звание',),
                'verbose_name_plural': 'звания',
                'ordering': ('title',),
            },
            bases=('abstracts.abstractdictionary',),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('abstractdictionary_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='abstracts.abstractdictionary')),
            ],
            options={
                'verbose_name': ('подразделение',),
                'verbose_name_plural': 'подразделения',
                'ordering': ('title',),
            },
            bases=('abstracts.abstractdictionary',),
        ),
        migrations.CreateModel(
            name='Management',
            fields=[
                ('abstractdictionary_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='abstracts.abstractdictionary')),
            ],
            options={
                'verbose_name': ('служба',),
                'verbose_name_plural': 'службы',
                'ordering': ('title',),
            },
            bases=('abstracts.abstractdictionary',),
        ),
    ]
