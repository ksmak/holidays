# Generated by Django 4.1.5 on 2023-02-01 07:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dictionaries', '0001_initial'),
        ('abstracts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('abstractmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='abstracts.abstractmodel')),
                ('number', models.IntegerField(verbose_name='номер')),
                ('date_enter', models.DateField(default=django.utils.timezone.now, verbose_name='дата выдачи')),
                ('date_start', models.DateField(default=django.utils.timezone.now, verbose_name='дата начало')),
                ('date_end', models.DateField(default=django.utils.timezone.now, verbose_name='дата конец')),
                ('last_name', models.CharField(max_length=150, verbose_name='фамилия')),
                ('first_name', models.CharField(max_length=150, verbose_name='имя')),
                ('middle_name', models.CharField(max_length=150, verbose_name='отчество')),
                ('job', models.CharField(max_length=150, verbose_name='должность')),
                ('place', models.CharField(blank=True, max_length=300, null=True, verbose_name='место выезда')),
                ('degree', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='dictionaries.degree', verbose_name='звание')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='dictionaries.department', verbose_name='подразделение')),
                ('management', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='dictionaries.management', verbose_name='служба')),
            ],
            options={
                'verbose_name': 'отпускное удостоверение',
                'verbose_name_plural': 'отпускные удостоверения',
                'ordering': ('date_enter', 'number'),
            },
            bases=('abstracts.abstractmodel',),
        ),
    ]
