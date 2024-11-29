from selenium_driverless import webdriver
from selenium_driverless.types.by import By
import asyncio
import os
from asynciolimiter import Limiter

proxy = 'pr.oxylabs.io:10000'

async def main():
    options = webdriver.ChromeOptions()
    # options.headless = True

    async with webdriver.Chrome(options) as driver:
        await driver.set_single_proxy(proxy)
        await driver.get('https://www.zara.com/uk/en/man-special-l2454.html?v1=2436970', wait_load=True)
        await asyncio.sleep(10)

        products = await driver.find_elements(By.CSS, 'div.product-grid-product__figure')

        urls = []
        for p in products:
            data = await p.find_element(By.CSS, 'a')
            link = await data.get_dom_attribute('href')
            urls.append(link)

        print(urls)

    pass

asyncio.run(main())