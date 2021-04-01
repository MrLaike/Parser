
HTML_TREE = {
  'title': './div[@class="items__description"]/a[@class="items__itemTitle"]',
}

SERVER_CONFIG = {
  'debug_mode': True,
  'host': '0.0.0.0',
}



def parse_obj(container):
  return {
    'title': container.xpath(TITLE_XPATH + '/text()').extract_first().strip(),
  }