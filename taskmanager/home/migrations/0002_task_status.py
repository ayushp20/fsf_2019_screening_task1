# Generated by Django 2.1.7 on 2019-03-13 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Planned', 'Planned'), ('In Progress', 'In Progress'), ('Done', 'Done')], default='Planned', max_length=100),
        ),
    ]
