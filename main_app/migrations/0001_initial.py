# Generated by Django 2.2.3 on 2019-12-24 22:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('class_id', models.AutoField(primary_key=True, serialize=False)),
                ('class_name', models.TextField()),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('spec_point', models.FloatField()),
                ('question', models.TextField()),
                ('diagram', models.BooleanField(default=False)),
                ('a', models.CharField(max_length=50)),
                ('b', models.CharField(max_length=50)),
                ('c', models.CharField(max_length=50)),
                ('d', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('quiz_id', models.AutoField(primary_key=True, serialize=False)),
                ('spec_range', models.TextField()),
                ('no_questions', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SpecReference',
            fields=[
                ('topic_number', models.FloatField(primary_key=True, serialize=False)),
                ('topic_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('term_id', models.AutoField(primary_key=True, serialize=False)),
                ('spec_point', models.FloatField()),
                ('term', models.TextField()),
                ('definition', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='QuizResult',
            fields=[
                ('result_id', models.AutoField(primary_key=True, serialize=False)),
                ('percentage_correct', models.FloatField()),
                ('quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Quiz')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ClassMembership',
            fields=[
                ('membership_id', models.AutoField(primary_key=True, serialize=False)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Class')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('assignment_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_set', models.DateField()),
                ('date_due', models.DateField()),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Class')),
                ('quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Quiz')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answer_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_answered', models.DateTimeField(auto_now=True)),
                ('is_correct', models.BooleanField()),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Question')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
