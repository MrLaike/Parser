from scrapy.spiders import Spider
from scrapy.spiders import CrawlSpider, Rule

class BaseSpider(Spider):
  name = 'base'

  # def start_requests(self):
  #   urls = ['https://stroy-s.org/catalog/53344/']

  #   for url in urls:
  #       yield scrapy.Request(url=url, callback=self.parse)


  def parse(self, response):
    for catalog in response.xpath('//div[@class="items__item lk__stocksItem "]'):
      yield {
        'title': catalog.xpath('./div[@class="items__description"]/a[@class="items__itemTitle"]/text()').extract_first(),
      }
