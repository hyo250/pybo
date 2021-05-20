#6WgY2p8IIMLTBrCkli1SyeuqcxQSoucZLhUI8o5rgvB5ocZ%2Bi6hoiElZrya9nlS462swX1unmcqxWxFbCWaD5A%3D%3D

import requests
import json
from bs4 import BeautifulSoup as bs
import sys

#http://apis.data.go.kr/1360000/AsosHourlyInfoService/getWthrDataList?serviceKey=인증키
# &numOfRows=10&pageNo=1&dataCd=ASOS&dateCd=HR&stnIds=108
# &endDt=20200310&endHh=01&startHh=01&startDt=20190120

def get_wdata(cname):
    page = requests.get('https://www.weather.go.kr/weather/observation/currentweather.jsp')
    if page.status_code != 200:
        sys.exit('데이터를 가져오지 못했습니다.')  # 응답이 없는 경우 프로그램 종료

    html=page.text
    soup=bs(html,'lxml')

    data=soup.find('table','table_develop3')

    tr_soup=data.find_all('tr')

    resultdata=[]
    for tmp in tr_soup:
        citydata= tmp.find_all('td')
        cnt=0
        cdata={}
        for temp1 in citydata:
            if cnt==0: #지역
                cdata['지역']=temp1.text
            elif cnt==1: #현재 일기
                cdata['현재 일기']=temp1.text
            elif cnt==5: #현재 기온
                cdata['현재기온']=temp1.text
            elif cnt == 8:  # 일강수
                cdata['일강수']=temp1.text
            cnt+=1

        if cdata !={}: #cdata가 비어이지 않으면
            resultdata.append(cdata)
            if cname in cdata['지역']:
                #print(cdata)
                return cdata

    return {} #if문에 해당하지 않아 데이터 못가져올경우 빈 딕셔너리 가져오게

#get_wdata('서울')