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

url = '(\\./forum.php?mod=attachment&aid=OTh8MTU4OTA3ZjZ8MTU0NzUyNTE2Mnw3NzM2Mnw5\\)'
print(url[3:-2])