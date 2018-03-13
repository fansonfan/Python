import urllib.request
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context


def getList():
    html =urllib.request.urlopen('https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-01-30&leftTicketDTO.from_station=XAY&leftTicketDTO.to_station=BJP&purpose_codes=ADULT').read()
    res = json.loads(html)
    return res['data']['result']

for i in getList():
    train_number=i.split('|')
    if train_number !='无':
        print("有票 车票详情")
        print("车次: %s\n出发时间: %s\n到达时间: %s\n剩余票数:%s" %(train_number[3],train_number[8],train_number[9],train_number[30]))
        break
    print(i)
