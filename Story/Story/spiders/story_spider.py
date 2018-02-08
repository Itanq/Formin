
from scrapy import Spider
from scrapy.http import Request
from scrapy.selector import Selector

from bs4 import BeautifulSoup

from Story.items import StoryItem

class StorySpider(Spider):
    name = "story"
    start_urls = [
        'http://www.hearead.com/thread-10'
    ]

    def parse(self, response):
        sel = Selector(response)
        infos = sel.xpath('//div[@class="thread_posts_list"]/table/tr')
        for info in infos:
            try:
                article_url = info.xpath("td/p[@class='title']/a/@href").extract()[0]
            except:
                print("")
            yield Request(article_url, callback=self.parse_item)

    def parse_item(self, response):

        item = StoryItem()

        sel = Selector(response)
        soup = BeautifulSoup(response.body)

        item['title'] = sel.xpath("//div[@class='floor_title cc']/h1/text()").extract()[0]
        item['author'] = sel.xpath("//div[@class='name']/a/text()").extract()[0]
        item['content'] = soup.find("div", {"class": "editor_content"}).get_text()

        yield item




