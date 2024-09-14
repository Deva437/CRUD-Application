# Generated by Django 4.2.14 on 2024-07-21 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=500, null=True)),
                ('task_description', models.TextField(max_length=200)),
                ('task_priority', models.CharField(choices=[('', 'none'), ('high', 'high'), ('medium', 'medium'), ('low', 'low')], default='none', max_length=106)),
                ('task_status', models.CharField(choices=[('', 'none'), ('inproces', 'inproces'), ('pending', ' pending'), ('complete', 'complete')], default='none', max_length=106)),
            ],
        ),
    ]
