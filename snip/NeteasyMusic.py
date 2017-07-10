#网易云音乐电台下载脚本
import requests
import re
import os

# -*- coding: UTF-8 -*-
url = "http://music.163.com/djradio"

# order 表示分页，0第一页，1第二页
querystring = {"id": "3059008", "order": "0", "_hash": "programlist", "limit": "100", "offset": "85"}

headers = {
    'cookie': "usertrack=ZUcIhletOVY2A1wJBLWRAg==; _ntes_nuid=653a7f9b92857aa8fc73128909d84145; _ntes_nnid=86749d91c232a2c25bf4a16fb26cfaaa,1471834946933; __utma=187553192.1901656414.1470970215.1471837184.1471837184.1; __utmz=187553192.1471837184.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __oc_uuid=10927190-681a-11e6-887f-b5fb1766cf7d; vjuids=-393dc2807.1570a82d9ca.0.11140a40d89e6; vjlast=1473350130.1473350130.30; NTES_REPLY_NICKNAME=wg1033755123%40126.com%7Cwg1033755123%7C%7C%7C%7C%7C1%7C-1; vinfo_n_f_l_n3=aa11b54bc88db327.1.1.1471837183546.1471837931510.1473350136315; P_INFO=wg1033755123@126.com|1473390513|0|mail126|00&99|bej&1473315640&carddav#bej&null#10#0#0|139202&0|mail126|wg1033755123@126.com; _ga=GA1.2.1901656414.1470970215; MUSIC_U=561ef7df8bf8af3de7fa88c7225da6faed19902973ea9ffddba0644f365fa45360cf58b4b9c44fe90eec4ddb48d141f6c599a636830af778fe2897047e8106fb; __csrf=bb2dc1940f73513f337b28178922491c; JSESSIONID-WYYY=ZsYXvSx05yCW%2F1A8OQw%2FCv2Hm3MdzXu%2BE%2BUhH92vvsCRF5lJ%2FV5NTiEfECI57QGbVpbecpx0j74d5zgk%2FWbwfrsP9AMZNA%5CHP2xTKZorkhw%5CsZJjVYcBUA%5C5hIUP7RBUtyU9ZHEnH%5CCIyEKVjbWNPIIwH%5CBDliBEswU8jE6d3%2FfoNRjl%3A1485054999479; _iuqxldmzr_=32; __utma=94650624.1901656414.1470970215.1484911093.1485053766.6; __utmb=94650624.2.10.1485053766; __utmc=94650624; __utmz=94650624.1484911093.5.4.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)",
    'cache-control': "no-cache",
    'postman-token': "101dcc2f-ebed-bfbc-0226-ff6ddbeab417"
}
## 网易云音乐要校验cookies的
response = requests.request("GET", url, headers=headers, params=querystring)

list_content = str(response.text)

# 正则匹配
result_list = re.findall(r"data-res-id=(.+?)\ data-res-fro", list_content)

def filterStr(string):
    if str.__contains__(string, "\""):
        return None
    else:
        return string


# filter处理后的是filter对象，留下满足条件的对象
simple_list = list(filter(filterStr, result_list))

# Python中的iter自带Collectors
re_re_list = ["http://music.163.com/#/program?id=" + iter_i for iter_i in simple_list]

# 在这个Main里面声明一个全局变量，下面直接用；如果是函数的话，函数体内还需要声明
global count
count = 0

for i in re_re_list:
    #使用uget提供的爬虫
    command = "/Users/wanggang/workspace/Tools/you-get/you-get -o /Users/wanggang/Music/AMSR/PPOMO " + i
    print(command)
    os.system(command)
    count = count + 1
    print("Num" + str(count) + "downloaded!")
