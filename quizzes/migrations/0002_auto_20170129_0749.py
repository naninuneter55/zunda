# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-28 22:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=256, verbose_name='回答内容')),
            ],
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': '問題', 'verbose_name_plural': '問題'},
        ),
        migrations.RenameField(
            model_name='question',
            old_name='answer',
            new_name='correct_answer',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.Question'),
        ),
    ]
