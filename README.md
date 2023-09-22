<div align="center">

# Mango Products Info
</div>
<div align="center">
Simple Scrapy project for scraping product data from the Mango website. It extracts information such as product name, color, price, and available sizes.
  
Keep in mind that if you want to run it on windows Scrapy-playwright needs additional configurations [Read More](https://scrapeops.io/python-scrapy-playbook/scrapy-playwright/)
</div>
<br>

Cloning the repository:
```bash
git clone https://github.com/vasskess/mango_products_info

```

Create a virtual environment and activate and activate it.

Install the requirements :
```bash
pip install -r requirements.txt

```
Navigate to:
```bash
cd scrapy_mango_data
```

Execute:
```bash
scrapy crawl products
```

<br>
<div style="letter-spacing: 2px;">
  
Wait until you see: ```INFO: Closing browser``` in the terminal. You should be able to see a ```product_data.jsonl``` file that is created in your ```scrapy_mango_data``` directory. Please note that the data in the ```.jsonl``` might not follow the order of the urls, since no custom ordering is implemented and also this is a bit hardcoded ```"item_price": response.css("span.sAobE.text-title-xl::text").get().split(" ")[1]``` and might have unexpected output if the price format is different ```(Example: 15.55 $)```, but for those two urls the format is ```(лв. 39.99) and (£ 39.99)``` and it works fine.
</div>
