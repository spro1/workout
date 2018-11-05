#!/usr/bin/env python3

import json
import app.scrap.scrap as scrap

json_path = '/home/yskim/webdir/config/dashboard.json'
json_data = {}

namu = scrap.namu_crawler()
naver = scrap.naver_news_crawler()
dc = scrap.dc_crawler()
river = scrap.river_temp()

json_data["namu"]=namu
json_data["naver"]=naver
json_data["dc"]=dc
json_data['river']=river

with open(json_path, 'w') as f:
    json.dump(json_data, f, ensure_ascii=False)
