import scrapy
import json
from scrapy_playwright.page import PageMethod


class MangoProductsSpider(scrapy.Spider):
    name = "products"
    product_data_list = []

    def start_requests(self):
        urls = [
            "https://shop.mango.com/gb/women/skirts-midi/midi-satin-skirt_17042020.html?c=99",
            "https://shop.mango.com/bg-en/men/t-shirts-plain/100-linen-slim-fit-t-shirt_47095923.html?c=07",
        ]
        for url in urls:
            yield scrapy.Request(
                url,
                meta=dict(
                    playwright=True,
                    playwright_include_page=True,
                    playwright_page_methods=[
                        PageMethod("wait_for_selector", "div.product-actions")
                    ],
                    errback=self.errback,
                ),
            )

    async def parse(self, response):
        page = response.meta["playwright_page"]
        await page.close()

        product_data = self.get_and_parse_products_info(response)
        self.product_data_list.append(product_data)
        yield product_data

    @staticmethod
    def get_and_parse_products_info(response):
        product_data = {
            "item_name": response.css("h1::text").get(),
            "item_color": response.css("span.colors-info-name::text").get(),
            "item_price": float(
                response.css("span.sAobE.text-title-xl::text").get().split(" ")[1]
            ),
            "item_sizes": response.css("span.text-title-m.gk2V5::text").getall(),
        }

        return product_data

    @staticmethod
    async def errback(failure):
        page = failure.request.meta["playwright_page"]
        await page.close()

    def closed(self, reason):
        with open("product_data.json", "w") as json_file:
            json.dump(self.product_data_list, json_file, ensure_ascii=False, indent=4)
