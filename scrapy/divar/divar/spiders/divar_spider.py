# Importing scrapy, The Essential library
import scrapy

# All the URLs of divar.ir is in this form
url = "https://divar.ir/v/-/{token}"

# I've extracted the pages' tokens and put them all in a text document named TOKENS
token_file = open(
    r'C:\Users\Administrator\Desktop\scrapy\divar\Tokens\TOKENS.txt', encoding='utf-8')
tokens = token_file.read().split(',')
token_file.close()


class DivarSpider(scrapy.Spider):
    # This is the name of the crawler
    # We use it when we type the crawling code in the CMD
    name = 'divar'
    start_urls = [url.format(token=token) for token in tokens]

    def parse(self, response):

        # dyc is Distance, Year, Color                                                        It works correctly
        dyc = response.css('div span.kt-group-row-item__value::text')

        distance = [(dyc[0].extract())]
        year = [int(dyc[1].extract())]
        color = [(dyc[2].extract())]

        # Link of each page
        link = [response.url]

        # We get Title and Value of many information here like chasis state, name, motor state and ...
        information = response.xpath(
            '//*[@id="app"]/div[1]/div[1]/div[1]/div[4]/div[@class="kt-base-row kt-base-row--large kt-unexpandable-row"]/div/*/*/text()').getall()
        information2 = response.xpath(
            '//*[@id="app"]/div[1]/div[1]/div[1]/div[4]/div[@class="kt-base-row kt-base-row--large kt-unexpandable-row"]/div/*/text()').getall()

        information = [information]
        list = [distance, year, color]
        yield {
            'Page link': link,
            'Infos': information,
            'test2': information2,
            'Distance Year Color': list
        }


# Code to start spider is: {spider folder location} scrapy crawl {name of the spider} -o {Name of file we want to build}.csv -t csv