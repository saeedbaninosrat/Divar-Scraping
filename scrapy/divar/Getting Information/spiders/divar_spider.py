# Importing scrapy, The Essential library
import scrapy
import os
# All the URLs of divar.ir is in this form
url = "https://divar.ir/v/-/{token}"

dir_path = os.path.dirname(os.path.abspath(__file__))

# I've extracted the pages' tokens and put them all in a text document named TOKENS
token_file = open(r'%s/TOKENS.txt' % dir_path, encoding='utf-8')
tokens = token_file.read().split('\n')
token_file.close()


class DivarSpider(scrapy.Spider):
    # This is the name of the crawler
    # We use it when we type the crawling code in the CMD
    name = 'divar'

    start_urls = [url.format(token=token) for token in tokens]
    custom_settings = {
        'CONCURRENT_REQUESTS': 30,
        'DOWNLOAD_DELAY': 1.2
    }

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
            '//*[@id="INERT-CONTAINER"]/div[1]/div/div/div[1]/div[4]/div[@class="kt-base-row kt-base-row--large kt-unexpandable-row"]/*/p/text()').getall()
        information2 = response.xpath(
            '//*[@id="INERT-CONTAINER"]/div[1]/div/div/div[1]/div[4]/div[@class="kt-base-row kt-base-row--large kt-unexpandable-row"]/div[2]/span/a/text()').getall()
        information = [information]
        list = [distance, year, color]

        yield {
            'Page link': link,
            'Infos': information,
            'test2': information2,
            'Distance Year Color': list
        }


# Code to start spider is: {spider folder location} scrapy crawl {name of the spider} -o {Name of file we want to build}.csv -t csv
