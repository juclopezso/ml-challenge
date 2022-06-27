import re
import asyncio
import aiohttp
from datetime import datetime
from app.main.model.item import Item
from .constants import ApisEnum, FileConfigEnum, countries_dict


async def handle_file(
    filepath, 
    encoding=FileConfigEnum.ENCODING.value, 
    separator=FileConfigEnum.SEPARATOR.value, 
    buffer_size=FileConfigEnum.DEFAULT_BUFFER_SIZE.value):
    """
        buffer_size: bytes/characters of data to be read at a time
    """

    # loop = asyncio.get_event_loop()

    items = []

    async with aiohttp.ClientSession() as session:
        with open(filepath, 'r') as file:
            tmp_lines = file.readlines(buffer_size)

            while tmp_lines:
                # print lines lenght base on buffer_size
                # print(len([line for line in tmp_lines]))
                for line in tmp_lines:
                    # loop.run_until_complete(process_line(line, items, encoding, separator))
                    # asyncio.run(process_line(line, items, encoding, separator, session))
                    await process_line(line, items, encoding, separator, session)

                tmp_lines = file.readlines(buffer_size)

        # loop.close()
    return items


async def process_line(line, items, encoding, separator, session):
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

    # item API call
    item_resp = await session.get(ApisEnum.ITEMS_API.value + country_code + item_code)
    # return if request is not ok
    if item_resp.status != 200:
        return

    item_resp = await item_resp.json()
    price = item_resp.get('price')
    # parse the date 
    start_time = datetime.strptime(item_resp.get('start_time'), '%Y-%m-%dT%H:%M:%S.%f%z') if item_resp.get('start_time') else None
    seller_id = item_resp.get('seller_id') # for users API
    category_id = item_resp.get('category_id') # fot categories API
    currency_id = item_resp.get('currency_id') # for currencies API

    # caterory API call
    category_name = None
    if category_id is not None:
        category_resp = await session.get(ApisEnum.CATEGORIES_API.value + str(category_id))
        if category_resp.status == 200: # ok
            category_json = await category_resp.json()
            category_name = category_json.get('name')
    
    # user API call
    nickname = None
    if seller_id is not None:
        user_resp = await session.get(ApisEnum.USERS_API.value + str(seller_id))
        if user_resp.status == 200:
            user_json = await category_resp.json()
            nickname = user_json.get('nickname')

    # currency API call
    currency_desc = None
    if currency_id is not None:
        currency_resp = await session.get(ApisEnum.CURRENCIES_API.value + str(currency_id))
        if currency_resp.status == 200:
            currency_json = await category_resp.json()
            currency_desc = currency_json.get('description')

    # create item object
    item = Item(
        id=item_code,
        site=country_code,
        price=price,
        start_time=start_time,
        name=category_name,
        description=currency_desc,
        nickname=nickname
    )

    # print(
    #     item_code, str(price), start_time, 
    #     "SELLER:",str(seller_id), "nick", nickname,
    #     "CATEGORY:", str(category_id), category_name,
    #     "CURRENCY:", str(currency_id), currency_desc
    # )

    items.append(item)
