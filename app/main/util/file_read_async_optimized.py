import re
import asyncio
import aiohttp
from datetime import datetime
from app.main.model.item import Item
from .constants import ApisEnum, FileConfigEnum, countries_dict


# TODO: config encoding
# TODO: test separator and encoding
async def handle_file(
    filepath, 
    encoding=FileConfigEnum.ENCODING.value, 
    separator=FileConfigEnum.SEPARATOR.value, 
    buffer_size=FileConfigEnum.DEFAULT_BUFFER_SIZE.value):
    """
        buffer_size: bytes/characters of data to be read at a time
    """

    items = []

    async with aiohttp.ClientSession() as session:
        with open(filepath, 'r') as file:
            tmp_lines = file.readlines(buffer_size)

            while tmp_lines:
                # print lines lenght base on buffer_size
                # print(len([line for line in tmp_lines]))
                items_group = await asyncio.gather(*(process_line(line, encoding, separator, session) for line in tmp_lines))
                for item in items_group:
                    if item is not None:
                        items.append(item)

                tmp_lines = file.readlines(buffer_size)

    return items


async def process_line(line, encoding, separator, session):
    country_code_raw, item_code_raw = line.split(separator)
    if country_code_raw is None or item_code_raw is None or country_code_raw == '' or item_code_raw == '':
        return
    # get the country code if it exists
    country_code = country_code_raw.strip() if countries_dict.get(country_code_raw.strip()) else None
    # get only the numbers of the item if exist and are well formatted
    item_code = re.findall(r'\d+', item_code_raw.strip())

    # return if country or item are not found or bad formated
    if country_code is None or len(item_code) == 0:
        return

    item_code = item_code[0]
    # print(country_code, item_code)
    return await fetch_item(item_code, country_code, session)


async def fetch_item(item_code, country_code, session):
    async with await session.get(ApisEnum.ITEMS_API.value + country_code + item_code) as resp:
        if int(resp.status) != 200:
            return

        item_resp = await resp.json()
        price = item_resp.get('price')
        # parse the date 
        start_time = datetime.strptime(item_resp.get('start_time'), '%Y-%m-%dT%H:%M:%S.%f%z') if item_resp.get('start_time') else None
        seller_id = item_resp.get('seller_id') # for users API
        category_id = item_resp.get('category_id') # fot categories API
        currency_id = item_resp.get('currency_id') # for currencies API

        category = await fetch_category(category_id, session)
        currency = await fetch_currency(currency_id, session)
        seller = await fetch_user(seller_id, session)

        return Item(
            id=item_code,
            site=country_code,
            price=price,
            start_time=start_time,
            name=category.get('name') if category else None,
            description=currency.get('description') if currency else None,
            nickname=seller.get('nickname') if seller else None
        )


async def fetch_category(id, session):
    async with await session.get(ApisEnum.CATEGORIES_API.value + str(id)) as resp:
        if resp.status == 200:
            return await resp.json()
        return None

async def fetch_user(id, session):
    async with await session.get(ApisEnum.USERS_API.value + str(id)) as resp:
        if resp.status == 200:
            return await resp.json()
        return None

async def fetch_currency(id, session):
    async with await session.get(ApisEnum.CURRENCIES_API.value + str(id)) as resp:
        if resp.status == 200:
            return await resp.json()
        return None
