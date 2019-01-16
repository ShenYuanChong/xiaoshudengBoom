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
        respHeaders = r1.headers
        for key in cookies.keys():
            if new_cookies.get(key) != None:
                cookies[key] = new_cookies.get(key)

        if (respHeaders.get('content-type') == 'text/html; charset=utf-8'):
            print('+-------------------------------------------警告------------------------------+\n')
            print('|                                                                             |\n')
            print('|                      ' + url  + ' |\n')
            print('|                         地址已经失效                                       |\n')
            print('|                                                                             |\n')
            print('|                                                                             |\n')
            print('+-----------------------------------------------------------------------------+')
            return 0, cookies, url
        if (respHeaders.get('content-type') == 'application/octet-stream'):
            temp = respHeaders.get('content-disposition')
            bText = temp.encode('ISO-8859-1')
            bbb = bText.decode('utf-8')
            p = re.compile(r'"(.*?)"')
            fileName = p.findall(bbb)
            f = open(fileName[0], 'wb')
            f.write(r1.content)
            f.close()
            return 1, cookies,url

        return 0, cookies, url

