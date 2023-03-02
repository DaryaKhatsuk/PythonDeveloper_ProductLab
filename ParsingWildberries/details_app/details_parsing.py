import asyncio

from arsenic import get_session
from arsenic.browsers import Chrome
from arsenic.errors import NoSuchElement
from arsenic.services import Chromedriver

from .models import ParsingResult


async def get_product_info(article):
    url = f'https://www.wildberries.ru/catalog/'
    service = Chromedriver(binary="C:\\Users\\Foxy\\PycharmProjects\\PythonDeveloper_ProductLab\\"
                                  "ParsingWildberries\\details_app\\chromedriver.exe")
    product_data = []
    async with get_session(service, Chrome()) as session:
        for index in article:
            print(index)
            await session.get(url=url + str(index) + '/detail.aspx')
            try:
                await asyncio.sleep(7)
                brands = await session.wait_for_element(1, '.seller-info__name')
                brand = await brands.get_text()
                title = await session.wait_for_element(1, '.product-page__header')
                text = await title.get_text()
                product_data.append({
                    'article': index,
                    'brand': brand,
                    'title': text,
                })
            except NoSuchElement:
                product_data.append({
                    'article': index,
                    'brand': 'not found',
                    'title': 'not found',
                })
            except Exception as e:
                print(e)
    for prod in product_data:
        product = ParsingResult(**prod)
        print(product)
