
import re


import threading
import requests
import json
import  urllib.request
# Create your views here.

from pachongApp.wechar.downLoad import cookie_bean, spider_Main
from django.shortcuts import render, HttpResponse, redirect

import urllib.request
# Create your views here.


def login(req):

    base_url = 'http://www.xiaoshudeng.com/plugin.php?id=xigua_login:login&infloat=yes&handlekey=wechat_bind1&inajax=1&ajaxtarget=fwin_content_wechat_bind1'

    response = urllib.request.urlopen(base_url)
    contest = response.read()
    pattern = re.compile(r'img .*?src="(.*?)"', re.S)
    pattern1 = re.compile(r'x.get(.*?),',re.S)
    contest = contest.decode('utf-8')
    #找到二维码
    ask = pattern1.findall(contest)
    ask = ask[0][2:-1]
    print(ask)
    #ask = ask[:-3]
    item_list = pattern.findall(contest)
    return render(req, 'login/login.html', {'weixinUrl': item_list[0],'askUrl':ask})  # 返回给login页面此参数




def check_login(req):
    tip = req.GET.get('tip')  # 标记是否扫码
    askUrl = req.GET.get('askUrl')
    # 自定义返回的json数据格式
    ret = {
        'code': 408,  # 初始值408代表没有任何操作
        'data': None
    }
    base_url = 'http://www.xiaoshudeng.com/'
    url1 = base_url + askUrl  # 字符串修饰
    r1 = requests.get(url1)  # 获取响应

    # 扫码之后，点击确定登录
    cookies = r1.cookies.get_dict()  # 获取确认登陆的cookie
    # 之后构建header 最重要是cookie

    if '<![CDATA[1]]>' in r1.text:
        r1 = requests.get(url1, cookies=cookies)  # 获取响应
        print("-------------------------<![CDATA[1]]>-------------------------\n")

    elif '<![CDATA[done]]>' in r1.text:
        # 扫码之后，点击确定登录
        print("-------------------------<![CDATA[done]]>-------------------------\n")
        cookieBean = cookie_bean.CookieBean()
        cookieBean.setCookies(cookies)
        #调用下载管理器  最好要新线程

        # try:
            #thread1 = myThread()
        spider_Main.SpiderMain().begin(20000,cookies)
        ret = {
            'code': 201,  # 初始值408代表没有任何操作
            'data': r1.text
        }
        # except:
        #     print("-------------------------线程报错-------------------------")
        #     ret = {
        #         'code': 408,  # 初始值408代表没有任何操作
        #         'data': r1.text
        #     }


    else:
        ret = {
            'code': 408,  # 初始值408代表没有任何操作
            'data': r1.text
        }

    return HttpResponse(json.dumps(ret))  # Json序列化返回


