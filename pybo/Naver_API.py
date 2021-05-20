# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
import json

def naverbook(bookname):
    
    client_id = "t8QA1gJsqoXBPrVV3UlY"
    client_secret = "byv9P3HRF3"
    
    encText = urllib.parse.quote(bookname)
    url = "https://openapi.naver.com/v1/search/book?query=" + encText # json 결과
    # url = "https://openapi.naver.com/v1/search/book.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        jsontemp=json.loads(response_body.decode('utf-8')) #문자열이니가 json.loads(만약 제이슨 딕셔너리였으면 json.dumps) 아닌가? 둘이 반댄가?
        #print(jsontemp)

        #for temp in jsontemp['items']:
        #    print(temp['author'])

        title=[]
        author=[]
        price=[]
        publisher=[]
        pubdate=[]

        for temp in jsontemp['items']:
            title.append(temp['title'])
            author.append(temp['author'])
            price.append(temp['price'])
            publisher.append(temp['publisher'])
            pubdate.append(temp['pubdate'])

        #print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)

    #print(title)
    return jsontemp

#오늘 하루 총 판매액
jsonstring = '''
{"date":"2021-05-11" , "data":[{"price":300 , "total":20},{"price":100 , "total":120}
,{"price":1200 , "total":52}]}
'''
res=json.loads(jsonstring)
#print(res['data'][0])
money=0
for i in res['data']:
    money=money+i['price']*i['total']

#print(money)


def navermovie(moviename):
    client_id = "t8QA1gJsqoXBPrVV3UlY"
    client_secret = "byv9P3HRF3"

    encText = urllib.parse.quote(moviename)
    url = "https://openapi.naver.com/v1/search/movie?query=" + encText  # json 결과
    # url = "https://openapi.naver.com/v1/search/book.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        jsontemp = json.loads(response_body.decode('utf-8'))  # 문자열이니가 json.loads(만약 제이슨 딕셔너리였으면 json.dumps) 아닌가? 둘이 반댄가?

        title = []
        userRating = []
        director = []
        actor=[]
        pubdate = []

        for temp in jsontemp['items']:
            title.append(temp['title'])
            userRating.append(temp['userRating'])
            director.append(temp['director'])
            actor.append(temp['actor'])
            pubdate.append(temp['pubDate'])
    else:
        print("Error Code:" + rescode)

    #print(title)
    return jsontemp

#print(navermovie("스파이럴"))

def navershop(name):
    client_id = "t8QA1gJsqoXBPrVV3UlY"
    client_secret = "byv9P3HRF3"

    encText = urllib.parse.quote(name)
    url = "https://openapi.naver.com/v1/search/shop?query="+encText  # json 결과 #오름차순shop?&sort=asc&query=
     # url = "https://openapi.naver.com/v1/search/book.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        jsontemp = json.loads(
            response_body.decode('utf-8'))  # 문자열이니가 json.loads(만약 제이슨 딕셔너리였으면 json.dumps) 아닌가? 둘이 반댄가?
        title = []
        lprice = []
        hprice = []
        image = []
        link = []

        for temp in jsontemp['items']:
             title.append(temp['title'])
             lprice.append(temp['lprice'])
             hprice.append(temp['hprice'])
             image.append(temp['image'])
             link.append(temp['link'])

    else:
        print("Error Code:" + rescode)
    return jsontemp

