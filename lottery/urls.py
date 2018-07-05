#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/8 12:35
# @Author  : eric
# @Site    : 
# @File    : urls.py
# @Software: PyCharm


from django.conf.urls import include, url

urlpatterns = [
    url(r'^accounts/login/$', 'lottery.account.login', name="login"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/accounts/login/'}, name="userlogout"),
    url(r'^$', 'lottery.views.index', name='home'),
    url(r'down/$', 'lottery.views.downfile', name='down-file-view'),  # url(r'^down')
    url(r'^lot5/$', 'lottery.views.lot5', name='home5'),
    url(r'^update5/$', 'lottery.views.update5', name='update5'),
    url(r'^lot5_10/$', 'lottery.views.lot5_10', name='home5_10'),
    url(r'^update5_10/$', 'lottery.views.update5_10', name='update5_10'),

    url(r'^cho5/$', 'lottery.views.cho5', name='cho5'),

    url(r'^lot4/$', 'lottery.views.lot4', name='home4'),
    url(r'^update4/$', 'lottery.views.update4', name='update4'),
    url(r'^cho4/$', 'lottery.views.cho4', name='cho4'),

    url(r'^lot3/$', 'lottery.views.lot3', name='home3'),
    url(r'^update3/$', 'lottery.views.update3', name='update3'),
    url(r'^cho3/$', 'lottery.views.cho3', name='cho3'),

    url(r'^lot2_1/$', 'lottery.views.lot2_1', name='home2_1'),
    url(r'^update2_1/$', 'lottery.views.update2_1', name='update2_1'),
    url(r'^cho2_1/$', 'lottery.views.cho2_1', name='cho2_1'),

    url(r'^lot2_t/$', 'lottery.views.lot2_t', name='home2_t'),
    url(r'^update2_t/$', 'lottery.views.update2_t', name='update2_t'),
    url(r'^cho2_t/$', 'lottery.views.cho2_t', name='cho2_t'),

    url(r'^lot1_t/$', 'lottery.views.lot1_t', name='home1_t'),
    url(r'^update1_t/$', 'lottery.views.update1_t', name='update1_t'),
    url(r'^cho1_t/$', 'lottery.views.cho1_t', name='cho1_t'),

    url(r'^lot1_1/$', 'lottery.views.lot1_1', name='home1_1'),
    url(r'^update1_1/$', 'lottery.views.update1_1', name='update1_1'),
    url(r'^cho1_1/$', 'lottery.views.cho1_1', name='cho1_1'),

    url(r'^lott_1/$', 'lottery.views.lott_1', name='homet_1'),
    url(r'^updatet_1/$', 'lottery.views.updatet_1', name='updatet_1'),
    url(r'^chot_1/$', 'lottery.views.chot_1', name='chot_1'),

    url(r'^lote_1/$', 'lottery.views.lote_1', name='homee_1'),
    url(r'^updatee_1/$', 'lottery.views.updatee_1', name='updatee_1'),
    url(r'^choe_1/$', 'lottery.views.choe_1', name='choe_1'),

    url(r'^lote_5/$', 'lottery.views.lote_5', name='homee_5'),
    url(r'^updatee_5/$', 'lottery.views.updatee_5', name='updatee_5'),
    url(r'^choe_5/$', 'lottery.views.choe_5', name='choe_5'),

    url(r'^lot1/$', 'lottery.views.lot1', name='home1'),
    url(r'^update1/$', 'lottery.views.update1', name='update1'),
    url(r'^cho1/$', 'lottery.views.cho1', name='cho1'),

    url(r'^lott_t/$', 'lottery.views.lott_t', name='homet_t'),
    url(r'^updatet_t/$', 'lottery.views.updatet_t', name='updatet_t'),
    url(r'^chot_t/$', 'lottery.views.chot_t', name='chot_t'),

    url(r'^lote_t/$', 'lottery.views.lote_t', name='homee_t'),
    url(r'^updatee_t/$', 'lottery.views.updatee_t', name='updatee_t'),
    url(r'^choe_t/$', 'lottery.views.choe_t', name='choe_t'),

    url(r'^lott/$', 'lottery.views.lott', name='homet'),
    url(r'^updatet/$', 'lottery.views.updatet', name='updatet'),
    url(r'^chot/$', 'lottery.views.chot', name='chot'),

    url(r'^lotj1/$', 'lottery.views.lotj1', name='homej1'),
    url(r'^updatej1/$', 'lottery.views.updatej1', name='updatej1'),

    url(r'^lotj2/$', 'lottery.views.lotj2', name='homej2'),
    url(r'^updatej2/$', 'lottery.views.updatej2', name='updatej2'),

    url(r'^result/$', 'lottery.views.result', name='result'),

    url(r'^upname/$', 'lottery.views.upname', name='upname-view'),
    url(r'^dellottyers/$', 'lottery.views.dellottyers', name='dellottyers-view'),

    url(r'^initialize/$', 'lottery.views.initialize', name='initialize'),

]
