import logging
import re
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