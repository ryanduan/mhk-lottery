#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/8 14:41
# @Author  : eric
# @Site    : 
# @File    : account.py
# @Software: PyCharm
from django import forms
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required

class LoginForm(forms.Form):
    username=forms.CharField(
        required=True,

        error_messages={'required':u'请输入用户名'},
        widget=forms.TextInput(
            attrs={
                'class':'',
                'placeholder': u"用户名",

            }
        ),
    )

    password=forms.CharField(
        required=True,

        error_messages={'required':u'请输入密码'},
        widget=forms.PasswordInput(
            attrs={
                'class':'',
                'placeholder':u'密码',
                'onfocus': "this.value = '';",
                'onblur': "if (this.value == '') {this.value = 'Password';}",
                'autocomplete': "off",
            }
        ),

    )

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u'请输入正确的用户名和密码')
        else:
            cleaned_data=super(LoginForm,self).clean()
        return self.cleaned_data


def login(request):
    error=[]
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('log/loggin.html', RequestContext(request, {'form': form, }))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return render_to_response('index.html', RequestContext(request))
            else:

                return render_to_response('log/loggin.html',
                                          RequestContext(request, {'form': form, 'password_is_wrong': True}))
        else:

            return render_to_response('log/loggin.html', RequestContext(request, {'form': form,'password_is_None':True }))