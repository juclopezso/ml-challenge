import re
import requests
from datetime import datetime
from app.main.model.item import Item
from .constants import ApisEnum, FileConfigEnum, countries_dict


def handle_file(
    filepath, 
    encoding=FileConfigEnum.ENCODING.value, 
    separator=FileConfigEnum.SEPARATOR.value, 
    buffer_size=FileConfigEnum.DEFAULT_BUFFER_SIZE.value):
    """
        buffer_size: bytes/characters of data to be read at a time
    """

    items = []

    with open(filepath, 'r') as file:
        tmp_lines = file.readlines(buffer_size)

        while tmp_lines:
            # print lines lenght base on buffer_size
            # print(len([line for line in tmp_lines]))
            for line in tmp_lines:
                process_line(line, items, encoding, separator)

            tmp_lines = file.readlines(buffer_size)

    return items


def process_line(line, items, encoding, separator):
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
    item_resp = requests.get(ApisEnum.ITEMS_API.value + country_code + item_code)
    # return if request is not ok
    if item_resp.status_code != 200:
        return

    item_resp = item_resp.json()
    price = item_resp.get('price')
    # parse the date 
    start_time = datetime.strptime(item_resp.get('start_time'), '%Y-%m-%dT%H:%M:%S.%f%z') if item_resp.get('start_time') else None
    seller_id = item_resp.get('seller_id') # for users API
    category_id = item_resp.get('category_id') # fot categories API
    currency_id = item_resp.get('currency_id') # for currencies API

    # caterory API call
    category_name = None
    if category_id is not None:
        category_resp = requests.get(ApisEnum.CATEGORIES_API.value + str(category_id))
        if category_resp.status_code == 200: # ok
            category_name = category_resp.json().get('name')
    
    # user API call
    nickname = None
    if seller_id is not None:
        user_resp = requests.get(ApisEnum.USERS_API.value + str(seller_id))
        if user_resp.status_code == 200:
            nickname = user_resp.json().get('nickname')

    # currency API call
    currency_desc = None
    if currency_id is not None:
        currency_resp = requests.get(ApisEnum.CURRENCIES_API.value + str(currency_id))
        if currency_resp.status_code == 200:
            currency_desc = currency_resp.json().get('description')

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

    # get the 
