BOT_NAME = 'shop_parser'

SPIDER_MODULES = ['shop_parser.spiders']
NEWSPIDER_MODULE = 'shop_parser.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'douyu (+http://www.yourdomain.com)'

DOWNLOADER_MIDDLEWARES = {
}

ITEM_PIPELINES = {
    'shop_parser.pipelines.JsonWithEncodingPipeline': 300,
}

LOG_LEVEL = 'INFO'

DOWNLOAD_DELAY = 1