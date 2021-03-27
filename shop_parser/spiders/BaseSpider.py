from scrapy.spiders import Spider
from scrapy import Request
from scrapy.spiders import CrawlSpider, Rule
from shop_parser.config import parse_obj

class BaseSpider(Spider):
  name = 'base'

  # def start_requests(self):
  #   urls = ['https://stroy-s.org/catalog/53344/']

  #   for url in urls:
  #       yield scrapy.Request(url=url, callback=self.parse)


  def parse(self, response):
    for catalog in response.xpath('//div[@class="items__item lk__stocksItem "]'):
      yield parse_obj(catalog)

    next_page = response.xpath('//a[@class="category__pagiItem category__pagiItem-next"]').attrib['href']
    if next_page is not None:
        next_page = response.urljoin(next_page)
        yield Request(next_page, callback=self.parse)
