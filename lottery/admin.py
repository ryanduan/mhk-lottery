#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/8 12:35
# @Author  : eric
# @Site    :
# @File    : admin.py
# @Software: PyCharm

from django.contrib import admin

# Register your models here.
from lottery.models import Person,Result

class PersonAdmin(admin.ModelAdmin):
    # 添加搜索框
    search_fields = ('name', 'tel', 'isWin','num','mWin','cWin')
    # 管理列表显示数据字段
    list_display = ('name', 'tel', 'isWin','num','mWin','cWin')
    # 添加过滤器，以下面字段进行过滤
    list_filter = ('name','isWin','mWin','cWin')
    # 新建面板中可以被编辑的字段
    fields = ('name', 'tel','num', 'isWin','mWin','cWin')

class ResultAdmin(admin.ModelAdmin):
    # 添加搜索框
    # search_fields = ('',)
    # 管理列表显示数据字段
    list_display = ('name', 'tel','num', 'awardname','isdel')
    # 添加过滤器，以下面字段进行过滤
    list_filter = ('name', 'awardname','isdel')
    # 新建面板中可以被编辑的字段
    fields = ('name', 'tel','num', 'awardname','isdel')


admin.site.register(Person,PersonAdmin)
admin.site.register(Result,ResultAdmin)