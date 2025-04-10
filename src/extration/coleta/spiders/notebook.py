import scrapy


class NotebookSpider(scrapy.Spider):
    name = "notebook"
    allowed_domains = ["saldaodainformatica.com.br"]
    start_urls = ["https://www.saldaodainformatica.com.br/notebook"]
    page_count = 1
    max_page = 10

    def parse(self, response):
        products = response.css('div.js-product')
        brands = ["Acer", "Lenovo", "Positivo", "Sony", "HP", "Dell", "Asus", "Samsung", "Apple"]
        

        for product in products:
            product_name = product.css('h2.product-title a::text').get(default='')   
            discount = product.css('div.desconto-pct:not(.frete-pct)::text').get(default='').replace('-','').strip()
            freight = product.css('div.desconto-pct::text').get(default='')
            discounted_price = product.css('p.preco-final::text').get(default='').replace('R$ ', '').replace('.','').replace(',','.').strip()
            full_price = product.css('span.z-preco-antigo::text').get(default='').replace('de: R$ ', '').replace('.','').replace(',','.').strip()
            page = response.css('a.disabled.js-search-link::text').get(default='').strip()
            brand_found = None
            if product_name:
                for brand in brands:
                    if brand.lower() in product_name.lower():
                        brand_found = brand
                        break
            yield {
                'brand': brand_found,
                'name': product_name,
                'discount': discount,
                'freight': freight,
                'discounted_price': float(discounted_price) if discounted_price else None,
                'full_price': float(full_price) if full_price else None,
                'page': int(page) if page.isdigit() else None
            }
        if self.page_count < self.max_page:
            next_page = response.css('a.next.js-search-link::attr(href)').get()
            if next_page:
                self.page_count += 1
                yield scrapy.Request(url=next_page, callback=self.parse)
