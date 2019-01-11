import re

import requests
import json
import http.cookiejar, urllib.request
# Create your views here.

from pachong.wechar.downLoad import cookie_bean
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
    #出现二维码同时  有一个长轮询
    #长轮询的返回结果为1  接着询问  返回不是1 返回不是1将接收cookie
    #用cookie 下载网站中资料
    #



    # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    # handler = urllib2.HTTPCookieProcessor(cookie)
    # 通过handler来构建opener
    # opener = urllib2.build_opener(handler)
    # 下边一句把上边两句合一块了
    #opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookies))




    ##xcode_list = re.findall('window.QRLogin.uuid = "(.*)";', response.text)  # 通过正则表达式，提取到对于的参数列表['YZzTdz9m_A==', 'YZzTdz9m_A==']
    ##req.session['xcode'] = xcode_list[0]  # 获取到参数，存入session内
    return render(req, 'login/login.html', {'weixinUrl': item_list[0],'askUrl':ask})  # 返回给login页面此参数




def check_login(req,):
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


    elif '<![CDATA[done]]>' in r1.text:
        # 扫码之后，点击确定登录

        url2= 'http://www.xiaoshudeng.com/forum.php?mod=attachment&aid=MjQ0NDB8YzUxNjk2ZDl8MTU0NzA5MjIwMnwwfDE2NjQ4'
        r1 = requests.get(url2, cookies=cookies,stream=False)  # 获取响应

        #储存cookie

        cookieBean = cookie_bean.CookieBean()
        cookieBean.setCookie(cookies)
        #调用下载管理器  最好要新线程

        fillName = r1.headers['filename']
        code = open(fillName, "wb")
        for chunk in r1.iter_content(chunk_size=1024*500):
            if chunk:
                code.write(chunk)
        code.close()
        ret = {
            'code': 201,  # 初始值408代表没有任何操作
            'data': r1.text
        }
        #之后试下载
        #http://www.xiaoshudeng.com/thread-16648-1-1.html  抓取此网页的下载链接
        #http://www.xiaoshudeng.com/forum.php?mod=attachment&aid=MjQ0NDB8YzUxNjk2ZDl8MTU0NzA5MjIwMnwwfDE2NjQ4
    else:
        ret = {
            'code': 408,  # 初始值408代表没有任何操作
            'data': r1.text
        }

    return HttpResponse(json.dumps(ret))  # Json序列化返回


