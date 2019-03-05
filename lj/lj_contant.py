import re


def house_type(str):
    return 'house_type', str


floor_pattern = re.compile(r'(\d+)[^\d]+')


def total_floor(str):
    return 'total_floor', floor_pattern.findall(str)[-1]


build_pattern = re.compile(r'\d+[.]*\d+')


def build_area(str):
    return 'build_area', build_pattern.findall(str)[-1]


def actual_area(str):
    l = build_pattern.findall(str)
    if l:
        return 'actual_area', l[-1]
    return 'actual_area', 0


def face_to(str):
    return 'face_to', str


def building_structure(str):
    return 'building_structure', str


def fix(str):
    return 'fix', str


def build_type(str):
    return 'build_type', str


def house_structure(str):
    return 'house_structure', str


def stairs_house_rate(str):
    return 'stairs_house_rate', str


def heating(str):
    return 'heating', str


def has_elevator(str):
    return 'has_elevator', str.find('有') >= 0


def house_year(str):
    l = floor_pattern.findall(str)
    if l:
        return 'house_year', l[-1]
    return 'house_year', 0


def villa_type(str):
    return 'villa_type', str


def water_type(str):
    return 'water_type', str


def electric_type(str):
    return 'electric_type', str


def gas_price(str):
    return 'gas_price', build_pattern.findall(str)[-1]


def shelf_time(str):
    return 'shelf_time', str


def last_buy_time(str):
    return 'last_buy_time', str


def trading_owner(str):
    return 'trading_owner', str


def use_type(str):
    return 'use_type', str


def house_life(str):
    return 'house_life', str


def property_owner(str):
    return 'property_owner', str


def has_mortgage(str):
    return 'has_mortgage', str.find('无') < 0


def house_spare(str):
    return 'house_spare', str


parse = {'房屋户型': house_type, '建筑面积': build_area, '所在楼层': total_floor, '户型结构': house_structure, '套内面积': actual_area,
         '建筑类型': build_type, '房屋朝向': face_to, '建筑结构': building_structure, '装修情况': fix, '梯户比例': stairs_house_rate,
         '供暖方式': heating, '配备电梯': has_elevator, '产权年限': house_year, '挂牌时间': shelf_time, '上次交易': last_buy_time,
         '交易权属': trading_owner, '房屋用途': use_type, '房屋年限': house_life, '产权所属': property_owner, '抵押信息': has_mortgage,
         '房本备件': house_spare, '用水类型': water_type, '用电类型': electric_type, '燃气价格': gas_price, '别墅类型': villa_type}

