__autor__ = 'Renato'
from scrapy.spiders import Spider
from scrapy.selector import  Selector
from searchResult import searchResultPages
from searchEngine import SearchEngineResult

class SpiderAddress(Spider):
    name = 'SpiderAddress'
    start_urls = []
    allowed_domains = ['google.com.br', 'google.com']
    keyword = None
    searchEngine = None
    selector = None

    def __init__(self, keyword, *args, **kwargs):
        super(SpiderAddress, self).__init__(*args, **kwargs)
        self.keyword = keyword.lower()
        self.searchEngine = 'google'
        self.selector = SearchEngineResult[self.searchEngine]
        pageUrls = searchResultPages(keyword, self.searchEngine , 1)
        for url in pageUrls:
            print(url)
            self.start_urls.append(url)

    def parse(self, response):
        for title in response.css('body'):
            yield {
            'endereco': title.css('body ::text').extract()
            }