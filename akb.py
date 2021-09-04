import datetime
import json
import os
import requests

def yujin():
    URL = 'http://www.akb48-china.com/trip/?tx_newsfrontedit_news[action]=ajaxdata'



    params = {
        'act': 'monthData',
        'year': '2021-09'
    }

    response_ = requests.post(URL, params=params)

    # print(response_.json())

    response = response_.json()
    now_time = datetime.datetime.now()
    bd = datetime.datetime.now().strftime('%Y%m%d')
    list = []
    opt=''
    # [('20210904', '综合运')】
    for i in response['data']:
        a = i['title']
        d = i['date']
        d = datetime.datetime.strptime(i['date'],"%Y-%m-%d")
        d= d.strftime("%Y%m%d")
        st=(f'{a}', f'{d}')
        st=str(st)+','
        opt=opt+st
        lsat='['+opt+']'
        lsat=lsat.replace('),]',')]')

        # dd = f"{a}"
        # ff=f"{d}"
        # dd = eval(dd)
        # list.append(dd)
        # list.append(ff)
        # return st
        # print(opt)
    return lsat


def sdf():
    s=yujin()
    dicee = eval(s)
    return dicee
    # print(dicee)



if __name__ == '__main__':

    print(sdf())