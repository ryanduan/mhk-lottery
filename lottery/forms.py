#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/8 17:01
# @Author  : eric
# @Site    : 
# @File    : forms.py
# @Software: PyCharm

from django import forms

class UpForm(forms.Form):
    upform = forms.FileField(required=True,error_messages={
        'required':u'必须选择一个导入文件',
        'invalid':u'上传文件是以xls结尾的excel'})