import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup

class HtmlParser(object):

    def parser(self, html):
        if html is None :
            return
        #解析页面中含有下载链接的链接
        pattern = re.compile(r'downurls.push(.*?);' )
        item_list = pattern.findall(html)
        self._get_new_urls(item_list)


    def _get_new_urls(self, item_list):
        new_urls = set()
        # http://www.xiaoshudeng.com/thread-17124-1-1.html
        # <a title="下载" class="downloadpdf xi2" target="_blank" href="./forum.php?mod=attachment&amp;aid=MjU3Mjd8M2YzN2RhNjV8MTU0NzE3ODI5Nnw3NzM2MnwxNzEyNA%3D%3D"> [下载]</a>

        #链接保存到set（）里
        f = open("downLoadUrl.txt", "w+")
        for link in item_list:
            new_urls.add(link)
            #同时写入到文件保存
            f.write(link +'\n')
            print(link +'\n')
        f.close()
        #返回set（）
        return new_urls