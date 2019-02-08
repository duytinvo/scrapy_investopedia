# Steps to build a crawler using scrapy

## Create a scrapy project
```bash
scrapy startproject scrapy_investopedia
cd scrapy_investopedia/
scrapy genspider investopedia_spider www.investopedia.com
```

## Edit __investopedia_spider.py__ file

This step depends on the html structure of each page

## Run the spider

```bash
scrapy crawl investopedia_spider -o investopedia_article.jl
```