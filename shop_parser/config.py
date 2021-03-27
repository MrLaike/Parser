
TITLE_XPATH = './div[@class="items__description"]/a[@class="items__itemTitle"]'

def parse_obj(container):
  return {
    'title': container.xpath(TITLE_XPATH + '/text()').extract_first().strip(),
  }