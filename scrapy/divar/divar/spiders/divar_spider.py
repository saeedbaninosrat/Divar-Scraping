import scrapy
import time


url = "https://divar.ir/v/-/{token}"

token_file = open(
    r'C:\Users\saeed\Desktop\scrapy\divar\tokens.txt', encoding='utf-8')
tokens = token_file.read().split(',')
token_file.close()


class DivarSpider(scrapy.Spider):
    name = 'divar'
    start_urls = [url.format(token=token) for token in tokens]

    def parse(self, response):
        # time.sleep(2)

        # # dyc is Distance, Year, Color                                                        It works correctly
        # dyc = response.css('div span.kt-group-row-item__value::text')                         

        # information = response.xpath('//div[@class="post-page__section--padded"]/div/text()').extract()

        test = response.css('*div[@class="kt-base-row kt-base-row--large kt-unexpandable-row"] div p::text')
        # brandmodel = response.xpath('//*[@id="app"]/div[1]/div[1]/div[1]/div[4]/div[@class="kt-base-row kt-base-row--large kt-unexpandable-row"]/div/span/a/text()' ).getall()
        # sellerid = response.xpath('//*[@id="app"]/div[1]/div[1]/div[1]/div[4]/div[@class="kt-base-row kt-base-row--large kt-unexpandable-row"]/div/span/a/text()').getall()

        # brandmodel = response.css('span a.kt-text-truncate::text')

        # informatione = response.css('div p.kt-unexpandable-row__value::text')

        # # span a.kt-text-truncate

        linkss = response.url

        # # brand_and_model =

        # distance = (dyc[0].extract())

        # year = int(dyc[1].extract())

        # color = (dyc[2].extract())

        # motorState = (informatione[0].extract())

        # chassisState = (informatione[1].extract())

        # guarantee = (informatione[2].extract())

        # gearboxModel = (informatione[3].extract())

        # paymentMode = (informatione[4].extract())

        # price = (informatione[5].extract())

        # block = (informatione[6].extract())

        # blocke = (informatione[7].extract())

        # warehouse = False if "ندارد" in dyc[3].extract() else True
        # parking = False if "ندارد" in dyc[4].extract() else True
        # elevator = False if "ندارد" in dyc[5].extract() else True
        # address = response.css(
        #     "div div.kt-page-title__subtitle--responsive-sized::text").extract()
        # price = response.css(
        #     "div p.kt-unexpandable-row__value::text").extract_first()

        yield {
            # 'Distance': distance,

            # 'Year': year,

            # 'Color': color,

            # 'MotorState': motorState,

            # 'ChassisState': chassisState,

            # 'Guarantee': guarantee,

            # 'GearboxModel': gearboxModel,

            # 'PaymentMode': paymentMode,

            # 'Price': price,

            # 'Block': block,

            'Token': linkss,

            # 'Infos': allinfos

            'test': test

            # 'testt' : brandmodel,

            # 'sellerid': [sellerid]
        }
