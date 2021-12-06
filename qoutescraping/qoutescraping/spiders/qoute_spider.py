import scrapy

class QuoteSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        "http://quotes.toscrape.com/"
    ]

    def parse(self, response):
        title = response.css("title::text").extract_first()
        #title = response.css("title::text")[0].extract()
 
        yield {
            "title" : title
        }