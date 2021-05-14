import os
from bs4 import BeautifulSoup as bs
import requests

def Mrank():
    page=requests.get('https://movie.naver.com/movie/running/current.nhn')
    html=page.text
    #print(html)
    soup=bs(html,'lxml')
    #print(soup)
    title_result=soup.find_all('dt','tit')
    #print(title_result)

    moviedata=[]

    result=soup.find_all('dl','lst_dsc')
    for tmp in result:
        mdata={}
        #제목
        tdata=tmp.find('dt','tit')
        tdata=tdata.find('a').text
        #평점
        star=tmp.find('div','star_t1')
        star=star.find('span','num').text
        #장르
        genre=tmp.find('dl','info_txt1')
        genre=genre.find('span','link_txt').text
        genre=genre.replace("\n", '').replace('\r','').replace('\t','')

        #print(genre)
        #print('='*50)
        mdata['title']=tdata
        mdata['star']=star
        mdata['genre']=genre
        moviedata.append(mdata)

    # -------------------# 썸네일 이미지 데이터 # -------------------#
    imgresult = soup.find_all('div','thumb')
    imgurl = []
    for temp in imgresult:
        url = temp.find('img')
        imgurl.append(url['src'])
        # print(url['src'])

    #print(imgurl)

    # print(imgresult)

    i=0
    for temp in moviedata:
        temp['img'] = imgurl[i]
        i+=1
        #print(temp)

    return moviedata