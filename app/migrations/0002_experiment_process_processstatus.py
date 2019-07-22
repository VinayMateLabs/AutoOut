# Generated by Django 2.2.1 on 2019-07-19 10:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='detection', max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'processes',
            },
        ),
        migrations.CreateModel(
            name='ProcessStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Not Started', max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'process_statuses',
            },
        ),
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('results_path', models.TextField(default='')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Dataset')),
                ('process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Process')),
                ('process_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ProcessStatus')),
            ],
            options={
                'db_table': 'experiments',
            },
        ),
    ]