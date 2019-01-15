import logging
import urllib.request
import requests
import  re

class Downloader(object):

    def __init__(self):
        self.host = 'http://www.xiaoshudeng.com/'
        self.link = ''

    #遍历网站正则匹配  保存
    def openWebCatchDownloadUrl(self,link,cookies):

        url = self.host + link
        r1 = requests.get(url,cookies=cookies)
        new_cookies = r1.cookies.get_dict()

        for key in cookies.keys():
            if new_cookies.get(key) != None:
                cookies[key] = new_cookies.get(key)


        if(r1.status_code != 200):
            f = open('400Url.txt', 'a+')
            f.write(url + '\n')
            f.close()
            return None,cookies
        if(r1.text.__contains__('<title>提示信息')):
            print('+-------------------------------------------警告------------------------------+\n')
            print('|                                                                             |\n')
            print('|                      '+url+' |\n')
            print('|                         cookie已经失效                                       |\n')
            print('|                                                                             |\n')
            print('|                                                                             |\n')
            print('+-----------------------------------------------------------------------------+')
            f = open('cookiesFail.txt', 'a+')
            f.write(url + '\n')
            f.close()
            return None, cookies
        f = open("BoomedUrl.txt", "a+")
        f.write(url + '\n')
        f.close()
        print('已经爆破' + url + '\n')
        return r1.text , cookies