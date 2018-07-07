#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/8 14:41
# @Author  : eric
# @Site    :
# @File    : views.py
# @Software: PyCharm

from django.shortcuts import render, render_to_response

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from lottery.forms import UpForm
from xmktlottery import settings
import os
import xlrd
from time import strftime, localtime
from django.shortcuts import render, render_to_response
from django.template import RequestContext
import random
from django.views.decorators.csrf import csrf_exempt
import json
from lottery.models import Person, Result
from django.db.models import Q


@login_required
def index(request):
    return render(request, 'index.html')


def downfile(request):
    from django.http import StreamingHttpResponse
    def file_iterator(file_name, chunk_size=512):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    the_file_name = "/var/work/lottery.zip"
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
    return response


@login_required
def lot5(request):
    res_num = Result.objects.filter(awardname='五等奖', isdel=0).count()
    if res_num < 41:
        if res_num == 0:
            toolot = '五等奖第一轮'

        elif res_num == 2:
            toolot = '五等奖第二轮'

        elif res_num == 7:
            toolot = '五等奖第三轮'
        elif res_num == 12:
            toolot = '五等奖第四轮'
        elif res_num == 17:
            toolot = '五等奖第五轮'
        elif res_num == 22:
            toolot = '五等奖第六轮'
        elif res_num == 25:
            toolot = '五等奖第七轮'
        elif res_num == 32:
            toolot = '五等奖第八轮'
        else:
            toolot = '五等奖第九轮'

        user_obj_list = Person.objects.filter(isWin=0)
        user_list = []
        for user_obj in user_obj_list:
            tel = user_obj.tel
            num = user_obj.num
            user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

        return render(request, 'lots/lot5.html', {
            'userlist': json.dumps(user_list),
            'toolot': toolot,
            'res_num': res_num
        })
    else:
        return render(request, 'lots/lot5.html', {
            'toolot': False,
            'res_num': res_num
        })


@login_required
def update5(request):
    res_num = Result.objects.filter(awardname='五等奖', isdel=0).count()
    if res_num < 42:
        obj_list = Person.objects.filter(isWin=0)
        user_list = []
        for user_obj in obj_list:
            tel = user_obj.tel
            num = user_obj.num
            user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

        if res_num < 40:
            win_list = random.sample(user_list, 5)
        else:
            win_list = random.sample(user_list, 2)
        for win in win_list:
            uid = win.get('id')
            p = Person.objects.get(id=uid)
            Person.objects.filter(id=uid).update(isWin=1)
            Result.objects.create(uid=uid, name=p.name, tel=p.tel, num=p.num, awardname='五等奖')

        toolnum = Result.objects.filter(awardname='五等奖', isdel=0).count()

        win_list.append({"toolnum": toolnum})
        return HttpResponse(json.dumps(win_list), content_type="application/json")

    else:
        return render(request, 'lots/lot5.html', {
            'toolot': False

        })


@login_required
def lot5_10(request):
    res_num = Result.objects.filter(awardname='五等奖', isdel=0).count()
    if res_num < 41:
        if res_num == 0:
            toolot = '五等奖第一轮'

        elif res_num == 2:
            toolot = '五等奖第二轮'

        elif res_num == 12:
            toolot = '五等奖第三轮'
        elif res_num == 22:
            toolot = '五等奖第四轮'
        else:
            toolot = '五等奖第五轮'

        user_obj_list = Person.objects.filter(isWin=0)
        user_list = []
        for user_obj in user_obj_list:
            tel = user_obj.tel
            num = user_obj.num
            user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

        return render(request, 'lots/lot5-10.html', {
            'userlist': json.dumps(user_list),
            'toolot': toolot,
            'res_num': res_num
        })
    else:
        return render(request, 'lots/lot5.html', {
            'toolot': False,
            'res_num': res_num
        })


@login_required
def update5_10(request):
    res_num = Result.objects.filter(awardname='五等奖', isdel=0).count()
    if res_num < 42:
        obj_list = Person.objects.filter(isWin=0)
        user_list = []
        for user_obj in obj_list:
            tel = user_obj.tel
            num = user_obj.num
            user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

        if res_num < 40:
            win_list = random.sample(user_list, 10)
        else:
            win_list = random.sample(user_list, 2)
        for win in win_list:
            uid = win.get('id')
            p = Person.objects.get(id=uid)
            Person.objects.filter(id=uid).update(isWin=1)
            Result.objects.create(uid=uid, name=p.name, tel=p.tel, num=p.num, awardname='五等奖')

        toolnum = Result.objects.filter(awardname='五等奖', isdel=0).count()

        win_list.append({"toolnum": toolnum})
        return HttpResponse(json.dumps(win_list), content_type="application/json")

    else:
        return render(request, 'lots/lot5.html', {
            'toolot': False

        })


@login_required
def cho5(request):
    chonum = Result.objects.filter(awardname='五等奖', isdel=0).count()

    return HttpResponse(chonum)


@login_required
def lot4(request):
    res_num = Result.objects.filter(awardname='四等奖', isdel=0).count()
    if res_num < 14:
        if res_num == 0:
            toolot = '四等奖第一轮'

        elif res_num == 2:
            toolot = '四等奖第二轮'
        elif res_num == 5:
            toolot = '四等奖第三轮'
        elif res_num == 8:
            toolot = '四等奖第四轮'
        else:
            toolot = '四等奖第五轮'

        user_obj_list = Person.objects.filter(isWin=0)
        user_list = []
        for user_obj in user_obj_list:
            tel = user_obj.tel
            num = user_obj.num
            user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

        return render(request, 'lots/lot4.html', {
            'userlist': json.dumps(user_list),
            'toolot': toolot,
            'toolnum': res_num
        })
    else:
        return render(request, 'lots/lot4.html', {
            'toolot': False

        })


@login_required
def update4(request):
    res_num = Result.objects.filter(awardname='四等奖', isdel=0).count()
    if res_num < 14:
        obj_list = Person.objects.filter(isWin=0)
        user_list = []
        for user_obj in obj_list:
            tel = user_obj.tel
            num = user_obj.num
            user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})
        if res_num < 12:

            win_list = random.sample(user_list, 3)
        else:
            win_list = random.sample(user_list, 2)
        for win in win_list:
            uid = win.get('id')
            p = Person.objects.get(id=uid)
            Person.objects.filter(id=uid).update(isWin=1)
            Result.objects.create(uid=uid, name=p.name, tel=p.tel, num=p.num, awardname='四等奖')
        toolnum = Result.objects.filter(awardname='四等奖', isdel=0).count()

        win_list.append({"toolnum": toolnum})
        return HttpResponse(json.dumps(win_list), content_type="application/json")
    else:
        # HttpResponse(json.dumps(win_list), content_type="application/json")
        return render(request, 'lots/lot4.html', {
            'toolot': False

        })


@login_required
def cho4(request):
    chonum = Result.objects.filter(awardname='四等奖', isdel=0).count()

    return HttpResponse(chonum)


@login_required
def lot3(request):
    res_num = Result.objects.filter(awardname='三等奖', isdel=0).count()
    if res_num < 8:
        if res_num == 0:
            toolot = '三等奖第一轮'
        elif res_num == 2:
            toolot = '三等奖第二轮'
        elif res_num == 4:
            toolot = '三等奖第三轮'
        else:
            toolot = '三等奖第四轮'

        user_obj_list = Person.objects.filter(isWin=0)
        user_list = []
        for user_obj in user_obj_list:
            tel = user_obj.tel
            num = user_obj.num
            user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

        return render(request, 'lots/lot3.html', {
            'userlist': json.dumps(user_list),
            'toolot': toolot,
            'toolnum': res_num
        })
    else:
        return render(request, 'lots/lot3.html', {
            'toolot': False

        })


def up_3(request):
    res_num = Result.objects.filter(awardname='三等奖', isdel=0).count()
    if res_num < 8:
        obj_list = Person.objects.filter(isWin=0)
        user_list = []

        for user_obj in obj_list:
            tel = user_obj.tel
            num = user_obj.num
            user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

        win_list = random.sample(user_list, 2)

        for win in win_list:
            uid = win.get('id')
            p = Person.objects.get(id=uid)
            Person.objects.filter(id=uid).update(isWin=1)
            Result.objects.create(uid=uid, name=p.name, tel=p.tel, num=p.num, awardname='三等奖')
        toolnum = Result.objects.filter(awardname='三等奖', isdel=0).count()

        win_list.append({"toolnum": toolnum})
        return HttpResponse(json.dumps(win_list), content_type="application/json")
    else:
        # HttpResponse(json.dumps(win_list), content_type="application/json")
        return render(request, 'lots/lot3.html', {
            'toolot': False

        })

@login_required
def update3(request):
    res_num = Result.objects.filter(awardname='三等奖', isdel=0).count()
    if res_num < 8:
        obj_list = Person.objects.filter(isWin=0, mWin=3)
        user_list = []
        res_list = []
        if obj_list:
            if len(obj_list) == 1:
                oth_obj = Person.objects.filter(isWin=0)
                for win_obj in obj_list:
                    tel = win_obj.tel
                    num = win_obj.num
                    res_dir = {'id': win_obj.id, 'name': win_obj.name, 'tel': tel, 'qnum': num}

                for user_obj in oth_obj:
                    tel = user_obj.tel
                    num = user_obj.num
                    user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

                win_list = random.sample(user_list, 1)
                win_list.append(res_dir)
            else:
                win_list = random.sample(obj_list, 2)

        else:
            obj_list = Person.objects.filter(isWin=0)
            for user_obj in obj_list:
                tel = user_obj.tel
                num = user_obj.num
                user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

            win_list = random.sample(user_list, 2)

        for win in win_list:
            uid = win.get('id')
            p = Person.objects.get(id=uid)
            Person.objects.filter(id=uid).update(isWin=1)
            Result.objects.create(uid=uid, name=p.name, tel=p.tel, num=p.num, awardname='三等奖')
        toolnum = Result.objects.filter(awardname='三等奖', isdel=0).count()

        win_list.append({"toolnum": toolnum})
        return HttpResponse(json.dumps(win_list), content_type="application/json")
    else:
        # HttpResponse(json.dumps(win_list), content_type="application/json")
        return render(request, 'lots/lot3.html', {
            'toolot': False

        })

@login_required
def cho3(request):
    chonum = Result.objects.filter(awardname='三等奖', isdel=0).count()

    return HttpResponse(chonum)


@login_required
def lot3(request):
    res_num = Result.objects.filter(awardname='三等奖', isdel=0).count()
    if res_num < 8:
        if res_num == 0:
            toolot = '三等奖第一轮'
        elif res_num == 2:
            toolot = '三等奖第二轮'
        elif res_num == 4:
            toolot = '三等奖第三轮'
        else:
            toolot = '三等奖第四轮'

        user_obj_list = Person.objects.filter(isWin=0)
        user_list = []
        for user_obj in user_obj_list:
            tel = user_obj.tel
            num = user_obj.num
            user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

        return render(request, 'lots/lot3.html', {
            'userlist': json.dumps(user_list),
            'toolot': toolot,
            'toolnum': res_num
        })
    else:
        return render(request, 'lots/lot3.html', {
            'toolot': False

        })


@login_required
def lot2_1(request):
    res_num = Result.objects.filter(awardname='二等奖', isdel=0).count()
    if res_num < 3:
        if res_num == 0:
            toolot = '二等奖第一轮'
        elif res_num == 1:
            toolot = '二等奖第二轮'
        else:
            toolot = '二等奖第三轮'

        return render(request, 'lots/lot2-1.html', {
            'toolot': toolot

        })

    else:
        return render(request, 'lots/lot2-1.html', {
            'toolot': False

        })


# @login_required
def cho2_1(request):
    chonum = Result.objects.filter(awardname='二等奖', isdel=0).count()

    return HttpResponse(chonum)


@login_required
def update2_1(request):
    res_num = Result.objects.filter(awardname='二等奖', isdel=0).count()
    if res_num < 3:
        obj_list = Person.objects.filter(isWin=0, mWin=2)
        if obj_list:
            pass
        else:
            obj_list = Person.objects.filter(isWin=0)
        user_list = []
        for user_obj in obj_list:
            tel = user_obj.tel
            num = user_obj.num
            user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

        win_list = random.sample(user_list, 1)

        for win in win_list:
            uid = win.get('id')
            p = Person.objects.get(id=uid)
            Person.objects.filter(id=uid).update(isWin=1)
            Result.objects.create(uid=uid, name=p.name, tel=p.tel, num=p.num, awardname='二等奖')
        toolnum = Result.objects.filter(awardname='二等奖', isdel=0).count()

        win_list.append({"toolnum": toolnum})
        return HttpResponse(json.dumps(win_list), content_type="application/json")
    else:
        # HttpResponse(json.dumps(win_list), content_type="application/json")
        return render(request, 'lots/lot2-1.html', {
            'toolot': False

        })

@login_required
def lot2_t(request):
    res_num = Result.objects.filter(awardname='二等奖', isdel=0).count()
    if res_num < 3:
        if res_num == 0:
            toolot = '二等奖第一轮'
        elif res_num == 1:
            toolot = '二等奖第二轮'
        else:
            toolot = '二等奖第三轮'

        return render(request, 'lots/lot2-t.html', {
            'toolot': toolot

        })

    else:
        return render(request, 'lots/lot2-t.html', {
            'toolot': False

        })


@login_required
def update2_t(request):
    res_num = Result.objects.filter(awardname='二等奖', isdel=0).count()
    obj_list = Person.objects.filter(isWin=0, mWin=2)
    if obj_list:
        pass
    else:
        obj_list = Person.objects.filter(isWin=0)
    if res_num < 3:

        user_list = []
        for user_obj in obj_list:
            tel = user_obj.tel
            num = user_obj.num
            user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

        win_list = random.sample(user_list, 1)

        for win in win_list:
            uid = win.get('id')
            p = Person.objects.get(id=uid)
            Person.objects.filter(id=uid).update(isWin=1)
            Result.objects.create(uid=uid, name=p.name, tel=p.tel, num=p.num, awardname='二等奖')
        toolnum = Result.objects.filter(awardname='二等奖', isdel=0).count()
        if toolnum == 1:

            win_list.append({"toolnum": True})
        else:
            win_list.append({"toolnum": False})
        return HttpResponse(json.dumps(win_list), content_type="application/json")
    else:
        # HttpResponse(json.dumps(win_list), content_type="application/json")
        return render(request, 'lots/lot2_t.html', {
            'toolot': False

        })


@login_required
def cho2_t(request):
    chonum = Result.objects.filter(awardname='二等奖', isdel=0).count()

    return HttpResponse(chonum)


@login_required
def lot2_1(request):
    res_num = Result.objects.filter(awardname='二等奖', isdel=0).count()
    if res_num < 3:

        toolot = '二等奖'

        user_obj_list = Person.objects.filter(isWin=0)
        user_list = []
        for user_obj in user_obj_list:
            tel = user_obj.tel
            num = user_obj.num
            user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

        return render(request, 'lots/lot2_1.html', {
            'userlist': json.dumps(user_list),
            'toolot': toolot,
            'toolnum': res_num
        })
    else:
        return render(request, 'lots/lot2_1.html', {
            'toolot': False

        })


@login_required
def update2_1(request):
    res_num = Result.objects.filter(awardname='二等奖', isdel=0).count()
    if res_num < 3:
        obj_list = Person.objects.filter(isWin=0)
        user_list = []
        for user_obj in obj_list:
            tel = user_obj.tel
            num = user_obj.num
            user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

        win_list = random.sample(user_list, 1)

        for win in win_list:
            uid = win.get('id')
            p = Person.objects.get(id=uid)
            Person.objects.filter(id=uid).update(isWin=1)
            Result.objects.create(uid=uid, name=p.name, tel=p.tel, num=p.num, awardname='二等奖')
        toolnum = Result.objects.filter(awardname='二等奖', isdel=0).count()

        win_list.append({"toolnum": toolnum})
        return HttpResponse(json.dumps(win_list), content_type="application/json")
    else:
        # HttpResponse(json.dumps(win_list), content_type="application/json")
        return render(request, 'lots/lot2_1.html', {
            'toolot': False

        })

@login_required
def cho2_1(request):
    chonum = Result.objects.filter(awardname='二等奖', isdel=0).count()

    return HttpResponse(chonum)


@login_required
def lot1_t(request):
    res_num = Result.objects.filter(awardname='一等奖', isdel=0).count()
    if res_num < 1:

        toolot = '一等奖'

        return render(request, 'lots/lot1_t.html', {
            'toolot': toolot

        })

    else:
        return render(request, 'lots/lot1_t.html', {
            'toolot': False

        })


@login_required
def update1_t(request):
    res_num = Result.objects.filter(awardname='一等奖', isdel=0).count()
    obj_list = Person.objects.filter(isWin=0, mWin=1)
    if obj_list:
        pass
    else:
        obj_list = Person.objects.filter(isWin=0)
    if res_num < 1:

        user_list = []
        for user_obj in obj_list:
            tel = user_obj.tel
            num = user_obj.num
            user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

        win_list = random.sample(user_list, 1)

        for win in win_list:
            uid = win.get('id')
            p = Person.objects.get(id=uid)
            Person.objects.filter(id=uid).update(isWin=1)
            Result.objects.create(uid=uid, name=p.name, tel=p.tel, num=p.num, awardname='一等奖')
        toolnum = Result.objects.filter(awardname='一等奖', isdel=0).count()
        if toolnum == 1:

            win_list.append({"toolnum": True})
        else:
            win_list.append({"toolnum": False})
        return HttpResponse(json.dumps(win_list), content_type="application/json")
    else:
        # HttpResponse(json.dumps(win_list), content_type="application/json")
        return render(request, 'lots/lot1_t.html', {
            'toolot': False

        })


@login_required
def cho1_t(request):
    chonum = Result.objects.filter(awardname='一等奖', isdel=0).count()

    return HttpResponse(chonum)


@login_required
def lott_t(request):
    res_num = Result.objects.filter(awardname='特等奖', isdel=0).count()
    if res_num < 1:

        toolot = '特等奖'

        return render(request, 'lots/lott_t.html', {
            'toolot': toolot

        })

    else:
        return render(request, 'lots/lott_t.html', {
            'toolot': False

        })


@login_required
def updatet_t(request):
    res_num = Result.objects.filter(awardname='特等奖', isdel=0).count()
    obj_list = Person.objects.filter(isWin=0, mWin=9)
    if obj_list:
        pass
    else:
        obj_list = Person.objects.filter(isWin=0)

    if res_num < 1:

        user_list = []
        for user_obj in obj_list:
            tel = user_obj.tel
            num = user_obj.num
            user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

        win_list = random.sample(user_list, 1)

        for win in win_list:
            uid = win.get('id')
            p = Person.objects.get(id=uid)
            Person.objects.filter(id=uid).update(isWin=1)
            Result.objects.create(uid=uid, name=p.name, tel=p.tel, num=p.num, awardname='特等奖')
        toolnum = Result.objects.filter(awardname='特等奖', isdel=0).count()
        if toolnum == 1:

            win_list.append({"toolnum": True})
        else:
            win_list.append({"toolnum": False})
        return HttpResponse(json.dumps(win_list), content_type="application/json")
    else:
        # HttpResponse(json.dumps(win_list), content_type="application/json")
        return render(request, 'lots/lott_t.html', {
            'toolot': False

        })


@login_required
def chot_t(request):
    chonum = Result.objects.filter(awardname='特等奖', isdel=0).count()

    return HttpResponse(chonum)


@login_required
def lote_t(request):
    # res_num = Result.objects.filter(awardname='加奖', isdel=0).count()

    toolot = '加奖'

    return render(request, 'lots/lote_t.html', {
        'toolot': toolot

    })


@login_required
def updatee_t(request):
    # res_num = Result.objects.filter(awardname='加奖', isdel=0).count()
    obj_list = Person.objects.filter(isWin=0, mWin=8)
    if obj_list:
        pass
    else:
        obj_list = Person.objects.filter(isWin=0)

    user_list = []
    for user_obj in obj_list:
        tel = user_obj.tel
        num = user_obj.num
        user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

    win_list = random.sample(user_list, 1)

    for win in win_list:
        uid = win.get('id')
        p = Person.objects.get(id=uid)
        Person.objects.filter(id=uid).update(isWin=1)
        Result.objects.create(uid=uid, name=p.name, tel=p.tel, num=p.num, awardname='加奖')
    toolnum = Result.objects.filter(awardname='加奖', isdel=0).count()

    win_list.append({"toolnum": True})

    return HttpResponse(json.dumps(win_list), content_type="application/json")


@login_required
def choe_t(request):
    chonum = Result.objects.filter(awardname='加奖', isdel=0).count()

    return HttpResponse(chonum)


@login_required
def lot1_1(request):
    res_num = Result.objects.filter(awardname='一等奖', isdel=0).count()
    if res_num < 1:

        toolot = '一等奖'

        user_obj_list = Person.objects.filter(isWin=0)
        user_list = []
        for user_obj in user_obj_list:
            tel = user_obj.tel
            num = user_obj.num
            user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

        return render(request, 'lots/lot1_1.html', {
            'userlist': json.dumps(user_list),
            'toolot': toolot,
            'toolnum': res_num
        })
    else:
        return render(request, 'lots/lot1_1.html', {
            'toolot': False

        })


@login_required
def update1_1(request):
    res_num = Result.objects.filter(awardname='一等奖', isdel=0).count()
    if res_num < 1:
        obj_list = Person.objects.filter(isWin=0, mWin=8)
        if obj_list:
            pass
        else:
            obj_list = Person.objects.filter(isWin=0)

        user_list = []
        for user_obj in obj_list:
            tel = user_obj.tel
            num = user_obj.num
            user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

        win_list = random.sample(user_list, 1)

        for win in win_list:
            uid = win.get('id')
            p = Person.objects.get(id=uid)
            Person.objects.filter(id=uid).update(isWin=1)
            Result.objects.create(uid=uid, name=p.name, tel=p.tel, num=p.num, awardname='一等奖')
        toolnum = Result.objects.filter(awardname='一等奖', isdel=0).count()

        win_list.append({"toolnum": toolnum})
        return HttpResponse(json.dumps(win_list), content_type="application/json")
    else:
        # HttpResponse(json.dumps(win_list), content_type="application/json")
        return HttpResponse("错误操作！")


@login_required
def cho1_1(request):
    chonum = Result.objects.filter(awardname='一等奖', isdel=0).count()

    return HttpResponse(chonum)


@login_required
def lott_1(request):
    res_num = Result.objects.filter(awardname='特等奖', isdel=0).count()
    if res_num < 1:

        toolot = '特等奖'

        user_obj_list = Person.objects.filter(isWin=0)
        user_list = []
        for user_obj in user_obj_list:
            tel = user_obj.tel
            num = user_obj.num
            user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

        return render(request, 'lots/lott_1.html', {
            'userlist': json.dumps(user_list),
            'toolot': toolot,
            'toolnum': res_num
        })
    else:
        return render(request, 'lots/lott_1.html', {
            'toolot': False

        })


@login_required
def updatet_1(request):
    res_num = Result.objects.filter(awardname='特等奖', isdel=0).count()
    if res_num < 1:
        obj_list = Person.objects.filter(isWin=0)
        user_list = []
        for user_obj in obj_list:
            tel = user_obj.tel
            num = user_obj.num
            user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

        win_list = random.sample(user_list, 1)

        for win in win_list:
            uid = win.get('id')
            p = Person.objects.get(id=uid)
            Person.objects.filter(id=uid).update(isWin=1)
            Result.objects.create(uid=uid, name=p.name, tel=p.tel, num=p.num, awardname='特等奖')
        toolnum = Result.objects.filter(awardname='特等奖', isdel=0).count()

        win_list.append({"toolnum": toolnum})
        return HttpResponse(json.dumps(win_list), content_type="application/json")
    else:
        # HttpResponse(json.dumps(win_list), content_type="application/json")
        return render(request, 'lots/lott_1.html', {
            'toolot': False

        })

@login_required
def chot_1(request):
    chonum = Result.objects.filter(awardname='特等奖', isdel=0).count()

    return HttpResponse(chonum)


@login_required
def lote_1(request):
    res_num = Result.objects.filter(awardname='加奖', isdel=0).count()

    toolot = '特等奖'

    user_obj_list = Person.objects.filter(isWin=0)
    user_list = []
    for user_obj in user_obj_list:
        tel = user_obj.tel
        num = user_obj.num
        user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

    return render(request, 'lots/lote_1.html', {
        'userlist': json.dumps(user_list),
        'toolot': toolot,
        'toolnum': res_num
    })


@login_required
def updatee_1(request):
    res_num = Result.objects.filter(awardname='加奖', isdel=0).count()

    obj_list = Person.objects.filter(isWin=0, mWin=8)
    if obj_list:
        pass
    else:
        obj_list = Person.objects.filter(isWin=0)

    user_list = []
    for user_obj in obj_list:
        tel = user_obj.tel
        num = user_obj.num
        user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

    win_list = random.sample(user_list, 1)

    for win in win_list:
        uid = win.get('id')
        p = Person.objects.get(id=uid)
        Person.objects.filter(id=uid).update(isWin=1)
        Result.objects.create(uid=uid, name=p.name, tel=p.tel, num=p.num, awardname='加奖')
    toolnum = Result.objects.filter(awardname='加奖', isdel=0).count()

    win_list.append({"toolnum": toolnum})
    return HttpResponse(json.dumps(win_list), content_type="application/json")


@login_required
def choe_1(request):
    chonum = Result.objects.filter(awardname='加奖', isdel=0).count()

    return HttpResponse(chonum)


@login_required
def lote_5(request):
    res_num = Result.objects.filter(awardname='加奖', isdel=0).count()

    toolot = '特等奖'

    user_obj_list = Person.objects.filter(isWin=0)
    user_list = []
    for user_obj in user_obj_list:
        tel = user_obj.tel
        num = user_obj.num
        user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

    return render(request, 'lots/lote_5.html', {
        'userlist': json.dumps(user_list),
        'toolot': toolot,
        'toolnum': res_num
    })


@login_required
def updatee_5(request):
    # res_num = Result.objects.filter(awardname='加奖', isdel=0).count()

    obj_list = Person.objects.filter(isWin=0)
    user_list = []
    for user_obj in obj_list:
        tel = user_obj.tel
        num = user_obj.num
        user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

    win_list = random.sample(user_list, 5)

    for win in win_list:
        uid = win.get('id')
        p = Person.objects.get(id=uid)
        Person.objects.filter(id=uid).update(isWin=1)
        Result.objects.create(uid=uid, name=p.name, tel=p.tel, num=p.num, awardname='加奖')
    toolnum = Result.objects.filter(awardname='加奖', isdel=0).count()

    win_list.append({"toolnum": toolnum})
    return HttpResponse(json.dumps(win_list), content_type="application/json")


@login_required
def choe_5(request):
    chonum = Result.objects.filter(awardname='加奖', isdel=0).count()

    return HttpResponse(chonum)


@login_required
def lot1(request):
    res_num = Result.objects.filter(awardname='一等奖', isdel=0).count()

    if res_num == 0:
        toolot = '一等奖'
        return render(request, 'lots/lot1.html', {
            'toolot': toolot

        })
    else:
        return render(request, 'lots/lot1.html', {
            'toolot': False

        })


def update1(request):
    res_num = Result.objects.filter(awardname='一等奖', isdel=0).count()
    obj_list = Person.objects.filter(isWin=0)
    if res_num == 0:

        user_list = []
        for user_obj in obj_list:
            tel = user_obj.tel
            num = user_obj.num
            user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

        win_list = random.sample(user_list, 1)

        for win in win_list:
            uid = win.get('id')
            p = Person.objects.get(id=uid)
            Person.objects.filter(id=uid).update(isWin=1)
            Result.objects.create(uid=uid, name=p.name, tel=p.tel, num=p.num, awardname='一等奖')
        # toolnum = Result.objects.filter(awardname='二等奖').count()

        win_list.append({"toolnum": False})
        return HttpResponse(json.dumps(win_list), content_type="application/json")
    else:
        # HttpResponse(json.dumps(win_list), content_type="application/json")
        return render(request, 'lots/lot1.html', {
            'toolot': False

        })


@login_required
def cho1(request):
    chonum = Result.objects.filter(awardname='一等奖', isdel=0).count()

    return HttpResponse(chonum)


@login_required
def lott(request):
    res_num = Result.objects.filter(awardname='特等奖', isdel=0).count()

    if res_num == 0:
        toolot = '特等奖'
        return render(request, 'lots/lott.html', {
            'toolot': toolot

        })
    else:
        return render(request, 'lots/lott.html', {
            'toolot': False

        })


@login_required
def updatet(request):
    res_num = Result.objects.filter(awardname='特等奖', isdel=0).count()
    obj_list = Person.objects.filter(isWin=0)
    if res_num == 0:
        user_list = []
        for user_obj in obj_list:
            tel = user_obj.tel
            num = user_obj.num
            user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

        win_list = random.sample(user_list, 1)

        for win in win_list:
            uid = win.get('id')
            p = Person.objects.get(id=uid)
            Person.objects.filter(id=uid).update(isWin=1)
            Result.objects.create(uid=uid, name=p.name, tel=p.tel, num=p.num, awardname='特等奖')
        # toolnum = Result.objects.filter(awardname='二等奖').count()

        win_list.append({"toolnum": False})
        return HttpResponse(json.dumps(win_list), content_type="application/json")
    else:
        # HttpResponse(json.dumps(win_list), content_type="application/json")
        return render(request, 'lots/lott.html', {
            'toolot': False

        })


@login_required
def chot(request):
    chonum = Result.objects.filter(awardname='特等奖', isdel=0).count()

    return HttpResponse(chonum)


@login_required
def lotj2(request):
    obj_list = Person.objects.filter(isWin=0)
    user_list = []
    for user_obj in obj_list:
        tel = user_obj.tel
        num = user_obj.num
        user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})
    toolot = '加奖'
    return render(request, 'lots/lotj2.html', {
        'userlist': json.dumps(user_list),
        'toolot': toolot,
    })


@login_required
def updatej2(request):
    obj_list = Person.objects.filter(isWin=0)
    user_list = []
    for user_obj in obj_list:
        tel = user_obj.tel
        num = user_obj.num
        name = user_obj.name
        l = name
        user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

    win_list = random.sample(user_list, 1)

    for win in win_list:
        uid = win.get('id')
        p = Person.objects.get(id=uid)
        Person.objects.filter(id=uid).update(isWin=1)
        Result.objects.create(uid=uid, name=p.name, tel=p.tel, num=p.num, awardname='加奖')
    # toolnum = Result.objects.filter(awardname='二等奖').count()

    # win_list.append({"toolnum": False})
    return HttpResponse(json.dumps(win_list), content_type="application/json")


@login_required
def lotj1(request):
    toolot = '加奖'
    return render(request, 'lots/lotj1.html', {
        'toolot': toolot

    })


@login_required
def updatej1(request):
    obj_list = Person.objects.filter(isWin=0)
    user_list = []
    for user_obj in obj_list:
        tel = user_obj.tel
        num = user_obj.num
        user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel, 'qnum': num})

    win_list = random.sample(user_list, 1)

    for win in win_list:
        uid = win.get('id')
        p = Person.objects.get(id=uid)
        Person.objects.filter(id=uid).update(isWin=1)
        Result.objects.create(uid=uid, name=p.name, tel=p.tel, num=p.num, awardname='加奖')
    # toolnum = Result.objects.filter(awardname='二等奖').count()

    # win_list.append({"toolnum": False})
    return HttpResponse(json.dumps(win_list), content_type="application/json")


# 继续抽奖（中奖不重复）
@login_required
@csrf_exempt
def dellottyers(request):
    request.session['where_from'] = request.META.get('HTTP_REFERER', '/')
    if request.method == 'POST':
        Result.objects.all().update(isdel=1)
    else:
        return HttpResponse("非法请求，请登录操作")
    return HttpResponseRedirect(request.session['where_from'])


# 数据上传
@login_required
def upname(request):
    username = request.user.username
    if request.method == 'POST':
        form = UpForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                xlsfiles = request.FILES.get('upform', '')
                filename = xlsfiles.name
                fname = os.path.join(settings.MEDIA_ROOT, 'uploads/users/%s' % strftime("%Y/%m/%d", localtime()),
                                     filename)
                if os.path.exists(fname):
                    os.remove(fname)
                dirs = os.path.dirname(fname)
                if not os.path.exists(dirs):
                    os.makedirs(dirs)

                if os.path.isfile(fname):
                    os.remove(fname)
                content = xlsfiles.read()
                fp = open(fname, 'wb')
                fp.write(content)
                fp.close()  # 上传文件完成

                # 删除旧数据

                Person.objects.all().delete()
                Result.objects.all().delete()
                # 导入新数据
                book = xlrd.open_workbook(fname)
                sheet = book.sheet_by_index(0)
                for row_index in range(1, sheet.nrows):
                    record = sheet.row_values(row_index, 0)
                    try:
                        print(record)
                        name = record[0].strip()
                        # phonenum = str(record[1]).rstrip(".0")
                        phonenum = str(record[1])

                        person = Person(name=name, tel=phonenum)
                        person.save()
                    except Person.DoesNotExist, e:
                        print e
                # successinfo = "上传"
                # success = True
                return HttpResponseRedirect('/')
                # """
                # return render_to_response('upname.html', {
                #     "title": '导入人员名单',
                #     'form': form,
                #     'successinfo': successinfo,
                #     'success': success,
                #     'username': username}, context_instance=RequestContext(request))"""
            except Exception, e:
                print e
        else:
            return render_to_response('upname.html', {
                "title": '导入人员名单',
                'form': form,
                'username': username}, context_instance=RequestContext(request))
    return render_to_response('upname.html', RequestContext(request))


@csrf_exempt
def initialize(request):
    request.session['where_from'] = request.META.get('HTTP_REFERER', '/')
    if request.method == 'POST':

        Person.objects.all().update(isWin=0, mWin=0, cWin=1)
    else:
        return HttpResponse("非法请求")
    return HttpResponseRedirect(request.session['where_from'])


@login_required
def result(request):
    rst_obj = Result.objects.all()
    rst_5_1 = rst_obj.filter(Q(awardname='五等奖'), Q(isdel=0)).order_by("-createtime")[:2]
    rst_5_2 = rst_obj.filter(Q(awardname='五等奖'), Q(isdel=0)).order_by("-createtime")[2:12]
    rst_5_3 = rst_obj.filter(Q(awardname='五等奖'), Q(isdel=0)).order_by("-createtime")[12:22]
    rst_5_4 = rst_obj.filter(Q(awardname='五等奖'), Q(isdel=0)).order_by("-createtime")[22:32]
    rst_5_5 = rst_obj.filter(Q(awardname='五等奖'), Q(isdel=0)).order_by("-createtime")[32:42]

    rst_4_1 = rst_obj.filter(Q(awardname='四等奖'), Q(isdel=0)).order_by("-createtime")[:2]
    rst_4_2 = rst_obj.filter(Q(awardname='四等奖'), Q(isdel=0)).order_by("-createtime")[2:5]
    rst_4_3 = rst_obj.filter(Q(awardname='四等奖'), Q(isdel=0)).order_by("-createtime")[5:8]
    rst_4_4 = rst_obj.filter(Q(awardname='四等奖'), Q(isdel=0)).order_by("-createtime")[8:11]
    rst_4_5 = rst_obj.filter(Q(awardname='四等奖'), Q(isdel=0)).order_by("-createtime")[11:14]

    rst_3_1 = rst_obj.filter(Q(awardname='三等奖'), Q(isdel=0)).order_by("-createtime")[:2]
    rst_3_2 = rst_obj.filter(Q(awardname='三等奖'), Q(isdel=0)).order_by("-createtime")[2:4]
    rst_3_3 = rst_obj.filter(Q(awardname='三等奖'), Q(isdel=0)).order_by("-createtime")[4:6]
    rst_3_4 = rst_obj.filter(Q(awardname='三等奖'), Q(isdel=0)).order_by("-createtime")[6:8]

    rst_2 = rst_obj.filter(Q(awardname='二等奖'), Q(isdel=0)).order_by("-createtime")[:3]
    rst_1 = rst_obj.filter(Q(awardname='一等奖'), Q(isdel=0)).order_by("-createtime")[:1]
    rst_t = rst_obj.filter(Q(awardname='特等奖'), Q(isdel=0)).order_by("-createtime")[:1]
    rst_j = rst_obj.filter(Q(awardname='加奖'), Q(isdel=0)).order_by("-createtime")

    return render(request, 'result.html', {'rst_5_1': rst_5_1 or None,
                                           'rst_5_2': rst_5_2 or None,
                                           'rst_5_3': rst_5_3 or None,
                                           'rst_5_4': rst_5_4 or None,
                                           'rst_5_5': rst_5_5 or None,
                                           'rst_4_1': rst_4_1 or None,
                                           'rst_4_2': rst_4_2 or None,
                                           'rst_4_3': rst_4_3 or None,
                                           'rst_4_4': rst_4_4 or None,
                                           'rst_4_5': rst_4_5 or None,
                                           'rst_3_1': rst_3_1 or None,
                                           'rst_3_2': rst_3_2 or None,
                                           'rst_3_3': rst_3_3 or None,
                                           'rst_3_4': rst_3_4 or None,
                                           'rst_2': rst_2 or None,
                                           'rst_1': rst_1 or None,
                                           'rst_t': rst_t or None,
                                           'rst_j': rst_j or None,
                                           })


@login_required
def refresh_name(req):
    """"""
    name_list = [
        "黄志强",
        "陈丽虹",
        "曾瑞安",
        "王奕元",
        "吴飞云",
        "邹燕凡",
        "潘晓明",
        "谢世杰",
        "苏立强",
        "罗欣文",
        "石泽浮",
        "陈志华",
        "林俊国",
        "由君龙",
        "庄艺",
        "刘伟文",
        "李添华",
        "何浩恩",
        "许方华",
        "黄俊杰",
        "杜建铭",
        "岑耀",
        "张锦华",
        "张炳添",
        "陈道凤",
        "戚国祥",
        "邓伟文",
        "陈雯雅",
        "庄海展",
        "邹少波",
        "陈观",
        "马奕娜",
        "陈础雄",
        "邱国伟",
        "陈冠行",
        "林志伟",
        "杨高政",
        "关伟萍",
        "许志文",
        "钟燕平",
        "陈文江",
        "郑仁明",
        "蔡惠霞",
        "谢文军",
        "许培连",
        "张伟杰",
        "林建明",
        "曾铧强",
        "陈幸跃",
        "杨永全",
        "陈立雄"
    ]
    for name in name_list:
        name = name.strip()
        if name:
            Person.objects.create(name=name)
    return HttpResponse('OK')
