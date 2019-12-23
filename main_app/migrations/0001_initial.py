# Generated by Django 2.2.3 on 2019-12-23 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spec_point', models.FloatField()),
                ('question', models.TextField()),
                ('diagram', models.BooleanField(default=False)),
                ('a', models.CharField(max_length=50)),
                ('b', models.CharField(max_length=50)),
                ('c', models.CharField(max_length=50)),
                ('d', models.CharField(max_length=50)),
                ('answer', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spec_point', models.FloatField()),
                ('term', models.TextField()),
                ('definition', models.TextField()),
            ],
        ),
    ]
