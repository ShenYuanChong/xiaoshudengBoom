import re

import chardet
from django.test import TestCase

# Create your tests here.
from pachongApp.wechar.downLoad import downloader_manager
from pachongApp.wechar.urlManager import html_parser


#组装link
# linkStr = 1
# while linkStr <20000:
#     link = 'thread-' + str(linkStr) + '-1-1.html'
#     html = downloader_manager.Downloader().openWebCatchDownloadUrl(link)
#     if html == None :
#         continue
#     html_parser.HtmlParser().parser(html)
#     linkStr = linkStr +1
#     print(link +'\n')
#
# link = 'thread-80-1-1.html'S
# html = downloader_manager.Downloader().openWebCatchDownloadUrl(link)
# html_parser.HtmlParser().parser(html)

tsxt = 'attachment; filename="éç¤¼è²éå¢2014-2015-2ç¬¬ä¸æ¬¡æèåä¸è¯­æè¯å·.pdf"'
bText = tsxt.encode('ISO-8859-1')
bbb = bText.decode('utf-8')
aaa = chardet.detect(bText)
print(aaa)
print(bbb)