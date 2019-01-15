import logging

from pachongApp.wechar.downLoad import cookie_bean, downloader_manager
from pachongApp.wechar.urlManager import url_manager, html_parser


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = downloader_manager.Downloader()
        self.cookie = cookie_bean.CookieBean().getCookies()
        self.htmlParser = html_parser.HtmlParser();

    def begin(self,n,cookies):
        #两部分
        # 1先遍历所有网站找到所有可以下载的链接，所有已经遍历的网站保存再数据库中，所有下载链接也保存在数据库中
        # 组装link
        linkStr = 9
        while linkStr < n:
            link = 'thread-' + str(linkStr) + '-1-1.html'
            linkStr = linkStr + 1
            html,cookies = downloader_manager.Downloader().openWebCatchDownloadUrl(link,cookies)
            if html == None:
                print('------------可能帖子删除跳过读取------------\n')
                continue
            html_parser.HtmlParser().parser(html)
            print('------------爆破完成------------\n')
        # 1-2把所有可以下载链接保存在数据库
        # 2.1 先把所有下载链接保存在url管理器中
        # 2.2 取出一个下载链接
        # 2.3 将cookie 和下载链接 传入下载器
        # 2.4 获取到下载文件 保存在本地
        # 2.5 循环再次




