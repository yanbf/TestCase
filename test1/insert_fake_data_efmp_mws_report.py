#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import random
import datetime as dt
from misc.util import makes
from model import *
DB11_master = create_engine(
    DB_STR_11, pool_recycle=3600, pool_size=50, poolclass=pool.SingletonThreadPool)
get_db11_master_cursor = get_cursor_factory(DB11_master)


PRINT_SQL = """INSERT INTO `efmp_mws_report` VALUES ('2016-07-12',5,'103-9942723-3899432','Peter Wu',45.63,'USD','B00WU721JE','TopQPS BIG ARM Car Mount Holder for iPhone 6/6s/Plus/5s/5c Galaxy S6/S5/S7 Edge/Note  4/5','Car Cradles & Mounts',2,10,'USD','1L-2XF3-8HCM','ATVPDKIKX0DER',1);"""
SQL = """INSERT INTO efmp_mws_report (log_time, pmd_account_id, order_id, buyer_name, order_amount, order_currency_code, asin, product_name, product_catelog, product_quantity, product_amount, product_currency_code, seller_sku, marketplaceid, new_buyer) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

ASIN_DICT = {
    'B019CX8PM0': 11.00,
    'B00ZCV7T6K': 12.00,
    'B01AJVN8VM': 7.00,
    'B00KGSPQDM': 7.00,
    'B013UDOEPA': 6.00,
    'B01GISQYR0': 26.00,
    'B00WU721JE': 27.37,
}
ASIN_NUM_LIST = ASIN_DICT.keys()

ASIN_PRODUCT_NAME_DICT = {
    "B019CX8PM0": """Car Mount, INCART&reg; Car Rearview Mirror Mount Truck Auto Bracket Holder Cradle for iPhone 6/6s/6s plus/ 5s/4s, Samsung Galaxy S6/S6 edge/S5/S4, Cell Phones,Smartphone, GPS / PDA / MP3 / MP4 devices""",
    "B00ZCV7T6K": """Car Charger, Lightning Car Charger®, Powerful 10 Amps - 4 USB Ports each with 2.4 amps Rapid Charger for iPhone 6 / 6 Plus, iPad Air / Mini, Samsung S6 , Edge, Sony, HTC and More""",
    "B01AJVN8VM": """Amaz247 Double Clip 360 Rotating Flexible Car Mount Cell Phone Holder Stand Car Accessories for iPhone, Samsung, LG, Nexus, HTC, Motorola, Sony & Other Smartphones, Black""",
    "B00KGSPQDM": """Docooler® 12V 12 LED Car Auto Interior Atmosphere Lights Decoration Lamp - Blue""",
    "B013UDOEPA": """Car Charger, Archeer Dual USB Car Charger Adapter(5v/3.4A output)with LCD Screen - Display for iPhone 6, 6 plus, 5 Samsung S6, S6 Edge and Android Devices""",
    "B01GISQYR0": """TopQPS BIG ARM Car Mount Holder for iPhone 6/6s/Plus/5s/5c Galaxy S6/S5/S7 Edge/Note 4/5 Black""",
    "B00WU721JE": """Zilu CM001 Universal Car Phone Mount, (Cell Phone Holder), Car Accessories For IPhone Samsung Galaxy Note and More -Black""",
}

Table = [
    'log_time',
    'pmd_account_id',
    'order_id',
    'buyer_name',
    'order_amount',
    'order_currency_code',
    'asin',
    'product_name',
    'product_catelog',
    'product_quantity',
    'product_amount',
    'product_currency_code',
    'seller_sku',
    'marketplaceid',
    'new_buyer'
]


def _random_product_asin_price(asin_list=None):
    if asin_list is None:
        asin_list = copy.copy(ASIN_DICT.keys())
    rand_asin = random.choice(asin_list)
    return rand_asin, ASIN_DICT[rand_asin]


def info_list_from_sql(sql=None):
    """info_list_from_sql
    :param sql_str: INSERT INTO `efmp_mws_report` VALUES ('2016-07-12',5,'103-9942723-3899432','Peter Wu',45.63,'USD','B00WU721JE','TopQPS BIG ARM Car Mount Holder for iPhone 6/6s/Plus/5s/5c Galaxy S6/S5/S7 Edge/Note  4/5','Car Cradles & Mounts',2,10,'USD','1L-2XF3-8HCM','ATVPDKIKX0DER',1);
    """
    if sql is None:
        sql = """INSERT INTO `efmp_mws_report` VALUES ('2016-07-12',5,'103-9942723-3899432','Peter Wu',45.63,'USD','B00WU721JE','TopQPS BIG ARM Car Mount Holder for iPhone 6/6s/Plus/5s/5c Galaxy S6/S5/S7 Edge/Note  4/5','Car Cradles & Mounts',2,10,'USD','1L-2XF3-8HCM','ATVPDKIKX0DER',1);"""
    sql = sql[sql.find('(')+1: sql.rfind(')')]
    res = [i.strip("'") for i in sql.split(',')]
    return copy.copy(res)


def sql_from_info_list(info_list):
    # for index, v in enumerate(info_list):
        # if isinstance(v, str):
            # info_list[index] = "'" + v + "'"
    sql = """INSERT INTO `efmp_mws_report` VALUES ('{}',5,'{}','{}',{},'USD','{}','{}','Car Cradles & Mounts',{},{},'USD','1L-2XF3-8HCM','ATVPDKIKX0DER',1);""".format(*[info_list[i] for i in [0,2,3,4,6,7,9,10]])
    return sql


def generate_date_range(beg_year, beg_month, beg_day,
                        end_year, end_month, end_day):
    beg_date = dt.datetime(beg_year, beg_month, beg_day)
    end_date = dt.datetime(end_year, end_month, end_day)
    while beg_date <= end_date:
        yield beg_date.strftime('%Y-%m-%d')    # year-mongth-day string
        beg_date += dt.timedelta(days=1)


def _get_incr_order_id(order_id):
    l = order_id.split('-')
    last_id = int(l[-1]) + 1
    return '-'.join([l[0], l[1], str(last_id)])


def _random_product_num():
    return random.randint(1, 8)


def _random_order_num():
    return random.randint(4, 8)


def _random_use_last_order_id():
    return random.choice(range(10)) < 3


def generate_sql_batch(use_sql_string=False):
    res_list = []
    info_list = copy.copy(info_list_from_sql())
    order_id = '107-9942723-390711'
    #for date in generate_date_range(2016,1,11,2016,6,22):
    for date in generate_date_range(2016,6,23,2016,7,6):

        today_asin_list = copy.copy(ASIN_NUM_LIST)
        cur_date_order_num = _random_order_num()
        last_asin = None

        for i in range(cur_date_order_num):
            # 一定概率上一个订单号一样，此时需要保证订单号一样的时候asin是不一样的
            use_last_id = _random_use_last_order_id() if i !=0 else False

            if not use_last_id:
                order_id = _get_incr_order_id(order_id)
            if use_last_id:
                today_asin_list.remove(last_asin)
            info_list[0] = date
            info_list[2] = order_id
            info_list[3] = makes(info_list[3])
            rand_asin, rand_price = _random_product_asin_price(today_asin_list)
            last_asin = rand_asin

            info_list[6] = rand_asin
            info_list[9] = _random_product_num()    # int
            info_list[10] = rand_price * info_list[9]
            info_list[4] = int(info_list[9]) * rand_price + 5.0    # 个数*单价+5
            info_list[7] = makes(ASIN_PRODUCT_NAME_DICT[rand_asin])

            if use_sql_string:
                res_list.append(sql_from_info_list(info_list))
            else:
                res_list.append(info_list)
    return res_list

def test_sql():
    s = """INSERT INTO `efmp_mws_report` VALUES ('2016-07-12',5,'103-9942723-3899432','Peter Wu',45.63,'USD','B00WU721JE','TopQPS BIG ARM Car Mount Holder for iPhone 6/6s/Plus/5s/5c Galaxy S6/S5/S7 Edge/Note  4/5','Car Cradles & Mounts',2,10,'USD','1L-2XF3-8HCM','ATVPDKIKX0DER',1);"""
    l = info_list_from_sql(s)
    print(sql_from_info_list(l))


def test():
    generate_sql_batch()

if __name__ == '__main__':
    sql_list = list(generate_sql_batch(True))
    #SQL = """INSERT INTO efmp_mws_report (log_time, pmd_account_id, order_id, buyer_name, order_amount, order_currency_code, asin, product_name, product_catelog, product_quantity, product_amount, product_currency_code, seller_sku, marketplaceid, new_buyer) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    with get_db11_master_cursor() as cursor:
        for sql in sql_list:
            print(sql)
            cursor.execute(sql)
