# Generated by Django 5.0.7 on 2024-07-17 01:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Actions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
                ('account_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='fin_analysis.account')),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Datas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('open', models.FloatField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('close', models.FloatField()),
                ('adj_close', models.FloatField()),
                ('volume', models.FloatField()),
                ('account_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='fin_analysis.account')),
                ('actions_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='fin_analysis.actions')),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddIndex(
            model_name='actions',
            index=models.Index(fields=['account_id', 'create_by', 'create_at'], name='fin_analysi_account_adc4db_idx'),
        ),
        migrations.AddIndex(
            model_name='datas',
            index=models.Index(fields=['account_id', 'create_by', 'create_at'], name='fin_analysi_account_4ffa51_idx'),
        ),
    ]