from urllib import request
import json
from lj.lj_url import *


def get_city_data():
    city_info = request.urlopen(city_url).read().decode('UTF-8')
    provinces = {}
    city_json = json.loads(city_info)
    if city_json['errno'] == 0:
        city_data_json = city_json['data']
        for k in city_data_json:
            province_json = city_data_json[k]
            citys = {}
            for ck in province_json:
                citys[province_json[ck]['name']] = province_json[ck]['url']
            provinces[k] = citys
    return provinces