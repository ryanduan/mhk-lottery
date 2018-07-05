# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u59d3\u540d')),
                ('tel', models.BigIntegerField(verbose_name='\u624b\u673a\u53f7\u7801')),
                ('num', models.CharField(default=100, max_length=50, verbose_name='\u5956\u5238\u53f7\u7801')),
                ('isWin', models.IntegerField(default=0, verbose_name='\u662f\u5426\u4e2d\u5956')),
                ('mWin', models.IntegerField(default=0)),
                ('cWin', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name_plural': '\u62bd\u5956\u4eba\u5458\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.IntegerField()),
                ('name', models.CharField(max_length=50, verbose_name='\u4e2d\u5956\u4eba\u59d3\u540d')),
                ('tel', models.CharField(max_length=50, verbose_name='\u4e2d\u5956\u4eba\u7535\u8bdd')),
                ('num', models.CharField(default=100, max_length=50, verbose_name='\u5956\u5238\u53f7\u7801')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='\u4e2d\u5956\u65f6\u95f4')),
                ('awardname', models.CharField(max_length=50, verbose_name='\u5956\u9879\u540d\u79f0')),
                ('isdel', models.IntegerField(default=0, verbose_name='\u662f\u5426\u88ab\u5220\u96641\u662f0\u5426')),
            ],
            options={
                'verbose_name_plural': '\u4e2d\u5956\u4eba\u5458\u4fe1\u606f',
            },
        ),
    ]
