# Generated by Django 3.1.3 on 2023-04-19 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0003_answer_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='create_time',
            new_name='create_date',
        ),
        migrations.AddField(
            model_name='answer',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]