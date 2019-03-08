from bs4 import BeautifulSoup
from lj.lj_contant import *
from lj.lj_city import *
import config.dao
import re

floor_pattern = re.compile(r'(\d+)[^\d]+')


def get_esf_data():
    provinces = get_city_data()
    for k in provinces:
        for ck in provinces[k]:
            page_num = 1
            cu = provinces[k][ck]
            while True:
                rsp = request.urlopen('%s/%s/pg%sco32/' %(cu, esf_url, page_num))
                if rsp.code != 200:
                    break
                html = rsp.read().decode('UTF-8')
                soup = BeautifulSoup(html, 'html.parser')
                lis = soup.find_all(name='li', attrs={'class': 'clear'})
                if len(lis) > 0:
                    for li in lis:
                        detail_url = li.find(name='div', attrs={'class': 'title'}).find('a')['href']
                        html = request.urlopen(detail_url).read().decode('UTF-8')
                        soup = BeautifulSoup(html, 'html.parser')
                        esf_basic = soup.find(name='div', attrs={'class': 'introContent'}).contents
                        basic_info = esf_basic[1].find(name='div', attrs={'class': 'content'}).find_all('li')
                        transaction_info = esf_basic[3].find(name='div', attrs={'class': 'content'}).find_all('li')
                        price_info = soup.find(name='div', attrs={'class': 'price'}).contents
                        esf_name = soup.find(name='div', attrs={'class': 'communityName'}).contents
                        esf_area = soup.find(name='div', attrs={'class': 'areaName'}).contents
                        esf_visit = soup.find(name='div', attrs={'class': 'visitTime'}).contents
                        esf_num = soup.find(name='div', attrs={'class': 'houseRecord'}).contents
                        house_info = soup.find(name='div', attrs={'class': 'houseInfo'}).contents
                        esf = {}
                        esf_price = {}
                        area = []
                        area.append(esf_area[2].contents[0].string)
                        area.append(esf_area[2].contents[2].string)
                        area.append(esf_area[2].contents[3][3:])
                        esf_description = soup.find(name='h1', attrs={'class': 'main'}).string
                        esf['province'] = k
                        esf['city'] = ck
                        esf['agency'] = '链家'
                        esf['description'] = esf_description
                        esf['name'] = esf_name[2].string
                        esf['area'] = ''.join(area)
                        esf['visit'] = esf_visit[2].string
                        esf['agency_num'] = esf_num[1].contents[0]
                        esf['attention_num'] = soup.find(name='span', attrs={'id': 'favCount'}).string
                        esf['show_num'] = soup.find(name='span', attrs={'id': 'cartCount'}).string
                        esf_price['total_price'] = price_info[0].string
                        esf_price['unit_price'] = price_info[2].find(name='span',
                                                                     attrs={'class': 'unitPriceValue'}).contents[0]
                        l = build_pattern.findall(house_info[2].contents[1].string)
                        build_year = 0
                        if l:
                            build_year = l[0]
                        esf['build_year'] = build_year
                        for b in basic_info:
                            key = b.contents[0].string
                            value = b.contents[1]
                            bk, bv = parse[key](value)
                            if not bk:
                                bk, bv = (key, value)
                            esf[bk] = bv
                        for b in transaction_info:
                            key = b.contents[1].string
                            value = b.contents[3].string
                            if value.find('\n') >= 0:
                                value = b.contents[3].attrs['title']
                            bk, bv = parse[key](value)
                            if not bk:
                                bk, bv = (key, value)
                            esf[bk] = bv
                        print(esf)

                    page_num += 1


def insert_house(house):
    pass

get_esf_data()
