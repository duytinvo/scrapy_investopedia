# -*- coding: utf-8 -*-
import scrapy
import string

alphabet = "1" + string.ascii_lowercase
base_url = "https://www.investopedia.com/terms/"
gurls = []
for ch in alphabet:
    curl = base_url + ch + '/'
    gurls.append(curl)


class InvestopediaSpiderSpider(scrapy.Spider):
    name = 'investopedia_spider'
    allowed_domains = ['www.investopedia.com']
    start_urls = gurls

    def parse(self, response):
        for item in response.xpath('//*/h3/a'):
            # term = item.xpath('text()').extract_first().strip()
            href = item.xpath('@href').extract_first().strip()
            # yield {term: href}
            yield response.follow(href, self.parse_article)

        next_page = response.xpath('//*[@id="Content"]/div[3]/div/div[1]/ul/li[@class="next"]/a/@href').extract_first()
        print(next_page)
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_article(self, response):
        title = response.xpath('//*[@id="article-heading_1-0"]/text()').extract_first().strip()
        block = response.xpath('//*[@class="comp mntl-sc-block mntl-sc-block-html"]')
        article = []
        for p in block:
            text = p.xpath('./p/text()').extract()
            text = " ".join(text)
            text = " ".join(text.split())
            if len(text.split()) > 0:
                article.append(text)
        if len(article) > 0:
            yield {title: "\n".join(article)}

