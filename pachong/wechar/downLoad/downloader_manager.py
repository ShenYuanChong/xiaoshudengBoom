import urllib.request
import  re

class Downloader(object):

    def __init__(self):
        self.host = 'http://www.xiaoshudeng.com/'
        self.link = ''

    #遍历网站正则匹配  保存
    def openWebCatchDownloadUrl(self):

        url = self.host + self.link
        r1 =urllib.request.urlopen(url)
        html = r1.read().decode('utf-8')
        return html