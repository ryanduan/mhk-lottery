#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/8 12:35
# @Author  : eric
# @Site    :
# @File    : models.py
# @Software: PyCharm

from django.db import models

# Create your models here.


class Person(models.Model):
    name=models.CharField(max_length=50,verbose_name=u'姓名')
    tel=models.BigIntegerField(verbose_name=u'手机号码')
    num=models.CharField(max_length=50,default=100,verbose_name=u'奖券号码')
    isWin=models.IntegerField(default=0,verbose_name=u'是否中奖')
    mWin=models.IntegerField(default=0)
    cWin=models.IntegerField(default=1)
    class Meta:
        verbose_name_plural=u'抽奖人员信息'

    def __unicode__(self):
        return self.name
    __str__=__unicode__


class Result(models.Model):
    uid=models.IntegerField()
    name=models.CharField(max_length=50,verbose_name=u'中奖人姓名')
    tel=models.CharField(max_length=50,verbose_name=u'中奖人电话')
    num=models.CharField(max_length=50,default=100,verbose_name=u'奖券号码')
    createtime=models.DateTimeField(auto_now_add=True,verbose_name=u'中奖时间')
    awardname=models.CharField(max_length=50,verbose_name=u'奖项名称')
    isdel=models.IntegerField(default=0,verbose_name=u'是否被删除1是0否')

    class Meta:
        verbose_name_plural=u'中奖人员信息'

    def __unicode__(self):
        return self.name
    __str__=__unicode__
