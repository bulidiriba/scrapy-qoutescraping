import scrapy

class QuoteSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        "http://quotes.toscrape.com/"
    ]

    # extract the all qoutes with the writer and the tag
    def parse(self, response):
        all_div_quotes = response.xpath("//div[@class='quote']") 
        # this returns all of the list of div with class quote, and that can be extracted in further, since extract method didn't applied here

        # loop through all the div qoute
        for quotes in all_div_quotes:
            # get the title inside the div quote, its span tag with class text
            title = quotes.xpath("span[@class='text']/text()").extract()
            # get the author inside the div quote, then inside the span, then the tag with class author
            author = quotes.xpath("span/small[@class='author']/text()").extract()
            # get the tag inside the div quote, then inside another div, then all the anchor tag with class tag
            tag = quotes.xpath("div/a[@class='tag']/text()").extract()
            print("----------------#############------------------")
            yield {
                "title" : title,
                "author" : author,
                "tag" : tag
            }