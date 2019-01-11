import urllib.request
import requests
import  re

class Downloader(object):

    def __init__(self):
        self.host = 'http://www.xiaoshudeng.com/'
        self.link = ''

    #遍历网站正则匹配  保存
    def openWebCatchDownloadUrl(self,link):

        url = self.host + link
        r1 = requests.get(url)

        #html1 =r1.content
        html = r1.text

        return html