from django.test import TestCase

# Create your tests here.
from pachong.wechar.downLoad import downloader_manager
from pachong.wechar.urlManager import html_parser



link = 'thread-17124-1-1.html'
html = downloader_manager.Downloader().openWebCatchDownloadUrl(link)
#html = 'downurls.push("./forum.php?mod=attachment&aid=MjU3Mjh8N2MyNzIyZmN8MTU0NzE4NzMyN3wwfDE3MTI0");'
html_parser.HtmlParser().parser(html)
