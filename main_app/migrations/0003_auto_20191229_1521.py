# Generated by Django 2.2.3 on 2019-12-29 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_question_correct_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.CharField(default='', max_length=1),
        ),
    ]
