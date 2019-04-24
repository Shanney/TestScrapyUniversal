from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


rules = {
    'china': (
        Rule(LinkExtractor(allow='article\/.*\.html', restrict_xpaths='//div[@id="left_side"]//div[@class="con_item"]'),
             callback='parse_item'),
        #Rule(LinkExtractor(restrict_xpaths='//div[@id="pageStyle"]//a[contains(., "下一页")]'))
    ),
    'tianyancha': (
        Rule(LinkExtractor(allow='company\/.*', restrict_xpaths='//div[contains(@class,"search-result-single")]//div[@class="header"]'),
             callback='parse_item'),
    )
}
