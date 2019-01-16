
import re


import threading

import chardet
import requests
import json
import  urllib.request
# Create your views here.
from django.utils.encoding import escape_uri_path

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


    if '<![CDATA[done]]>' in r1.text:
        # 扫码之后，点击确定登录
        print("-------------------------<![CDATA[done]]>-------------------------\n")
        fname = 'downLoadUrl.txt'
        f1 = open(fname, 'r')
        line = f1.readline()
        while line:
            count = 1
            tip = None
            url = 'http://' + line[:-1]
            r1 = requests.get(url, cookies=cookies)
            new_cookies = r1.cookies.get_dict()
            respHeaders = r1.headers
            for key in cookies.keys():
                if new_cookies.get(key) != None:
                    cookies[key] = new_cookies.get(key)

            # 地址失效
            if (respHeaders.get('content-type') == 'text/html; charset=utf-8'):
                print('+-------------------------------------------警告------------------------------+\n')
                print('|                                                                             |\n')
                print('|                      ' + url + ' |\n')
                print('|                         地址已经失效                                       |\n')
                print('|                                                                             |\n')
                print('|                                                                             |\n')
                print('+-----------------------------------------------------------------------------+')
                tip = 0
            if (respHeaders.get('content-type') == 'application/octet-stream'):
                print(url + '\n')
                temp = respHeaders.get('content-disposition')
                bText = temp.encode('ISO-8859-1')
                bbb = bText.decode('utf-8')
                p = re.compile(r'"(.*?)"')
                fileName = p.findall(bbb)
                mulu = "g:/student/"+fileName[0]
                f = open(mulu, 'wb')
                f.write(r1.content)
                f.close()
                tip = 1
            f = open('downLoadInfo.txt', 'w+')
            f.write(str(tip) + '|' + str(count) + '|' + url + '\n')
            f.close()
            count = count + 1
            line = f1.readline()


    return HttpResponse(json.dumps(ret))  # Json序列化返回


