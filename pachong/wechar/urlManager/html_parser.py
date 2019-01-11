from bs4 import BeautifulSoup

class HtmlParser(object):

    def parser(self, html,download_url):
        if html is None :
            return

        soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
        self._get_new_urls(download_url, soup)


    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # /view/123.htm
        links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls