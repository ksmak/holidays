# Generated by Django 4.1.5 on 2023-01-17 05:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dictionaries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='номер')),
                ('first_name', models.CharField(max_length=150, verbose_name='имя')),
                ('last_name', models.CharField(max_length=150, verbose_name='фамилия')),
                ('middle_name', models.CharField(max_length=150, verbose_name='отчество')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='создан')),
                ('change_date', models.DateTimeField(auto_now=True, verbose_name='изменен')),
                ('change_user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='change_user', to=settings.AUTH_USER_MODEL, verbose_name='кем изменен')),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='create_user', to=settings.AUTH_USER_MODEL, verbose_name='кем создан')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='dictionaries.department', verbose_name='подразделение')),
                ('management', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='dictionaries.management', verbose_name='служба')),
            ],
        ),
    ]