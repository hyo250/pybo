from flask import Blueprint, render_template, url_for, request, jsonify
from werkzeug.utils import redirect

from pybo.models import Question, Answer, User, BTS_vote
from datetime import datetime
from pybo import db #init.py에서 db=SQLAlchemy()
from pybo.movieapi import Mrank
from pybo.Naver_API import navermovie, navershop
from pybo.weatherapi import get_wdata

bp=Blueprint('main', __name__, url_prefix='/')


#블루프린트를 쓰기 시작하면 이렇게 쓰세여
@bp.route('/test')
def test():
    for i in range(100):
        q=Question(subject='테스트 데이터[%03d]'%i, content='내용없음', create_date=datetime.now())
        db.session.add(q)
    db.session.commit()
    
    return redirect(url_for('main.index'))

@bp.route('/hello') #main/뒤에 호출할 것 입력하기. /hello면 127.0.0.1:5000/main/hello 이런식.
def hello_pybo():
    ####쿼리문 확인하기 ######
    # result=Question.query.all()
    # print(result)
    # for temp in result:
    #     print(temp.id)
    #     print(temp.subject)
    #     print(temp.content)

    #######특정 조건 만족하는 쿼리문 불러오기 ########3
    # result1 = Question.query.all()
    # title=[]
    # for temp in result1:
    #     if temp.id<= 5:
    #         title.append(temp.subject)
    #
    # print('subject 리스트 입니다.: ', title)

    ######### 위의 for 문 한줄로 써보기 (filter 이용)##########3
    #result=Question.query.filter(Question.id<6).all()
    #print(result)

    ########1개만 가져올때는 get 쓰기########
    #result=Question.query.get(1);print(result) #id(primary_key)=1인 것 가져옴

    ###########검색 기능##########
    #result=Question.query.filter(Question.subject.like('%무엇%')).all()
    #print('무엇 검색시 나오는 것들: ', result)

    #############아이디 가져와서 내용 바꾸기#########
    result=Question.query.get(1)
    result.subject='파이보 정말 쉽지 않네'
    db.session.commit()
    #print(result)

    # q = Question(subject='pybo가 무엇인가요?', content='pybo에 대해서 알고 싶습니다. ', create_date=datetime.now())
    # a = Question(subject='python 재밌나요?', content='python에 대해서 알고 싶습니다. ', create_date=datetime.now())
    # b = Question(subject='java가 무엇인가요?', content='java에 대해서 알고 싶습니다. ', create_date=datetime.now())
    # c = Question(subject='spring가 무엇인가요?', content='spring에 대해서 알고 싶습니다. ', create_date=datetime.now())
    # d = Question(subject='R이 무엇인가요?', content='R에 대해서 알고 싶습니다. ', create_date=datetime.now())
    # e = Question(subject='송중기 38살 실화?', content='송중기에 대해서 알고 싶습니다. ', create_date=datetime.now())
    # f = Question(subject='빈센조 시즌 2나오나요?', content='빈센조 못잃어... ', create_date=datetime.now())
    # g = Question(subject='오늘 날씨 어떤가요?', content='날씨에 대해서 알고 싶습니다. ', create_date=datetime.now())
    # h = Question(subject='방금 나온 노래가 무엇인가요?', content='그 음악에 대해서 알고 싶습니다. ', create_date=datetime.now())
    # i = Question(subject='플라스크가 무엇인가요?', content='플라스크에 대해서 알고 싶습니다. ', create_date=datetime.now())

    # db.session.add(q);db.session.add(a);db.session.add(b);db.session.add(c);db.session.add(d)
    # db.session.add(e);db.session.add(f);db.session.add(g);db.session.add(h);db.session.add(i)
    # db.session.commit()

    ###########쿼리문의 삭제########
    #result=Question.query.get(2) #id=2인 것 삭제
    #db.session.delete(result)
    #db.session.commit()

    #########쿼리문 답변달기 ########33
    # q = Question.query.get(4)
    # a = Answer(question=q, content='아직 당신에겐 이릅니다.', create_date=datetime.now())
    # db.session.add(a)  # 더하고
    # db.session.commit()  # 커밋

    ##1번 질문에 대한 답변 데이터 가져오기.
    #방법1)
    # answer=Answer.query.get(1)
    #print('1번 질문 답입니다: ' , answer)
    #방법2)
    #q = Question.query.get(1)
    #result = Answer.query.filter(Answer.question_id == 1).all()
    #print('1번 답:', result)
    #방법3(question이 지워지면 같이 자동으로 지워지는 답변들임)
    # q=Question.query.get(1)
    # result=q.answer_set
    # print(result)

    ##미션1)5번 질문에 대한 답 3개 만들기
    # q = Question.query.get(5)
    # a = Answer(question=q, content='시각화, 통계하기 좋은 거', create_date=datetime.now())
    # b = Answer(question=q, content='부성순 강사님과 배움', create_date=datetime.now())
    # c = Answer(question=q, content='알이 알이지', create_date=datetime.now())

    #db.session.add(a); db.session.add(b); db.session.add(c)
    #db.session.commit()


    ##미션2)5번 질문을 역참조하는 답변 출력
    #q = Question.query.get(5)
    #result = q.answer_set
    #print('5번질문 역참조 답변들: ', result)

    ##미션3)5번 질문을 삭제하고 5번 질문을 역참조하는 답변 확인
    #db.session.delete(q)
    #db.session.commit() #id에 null로 뜸

    ###class user ########
    a1 = User(pw='apple', name='송중기', age='37', address='이탈리아', birth='1985-9-19', gender='남자', create_date=datetime.now())
    a2 = User(pw='banana', name='이곰돌', age='12', address='서울', birth='2010-1-3', gender='남자', create_date=datetime.now())
    a3 = User(pw='cheese', name='김제리', age='27', address='부산',birth='1995-9-19', gender='남자', create_date=datetime.now())
    a4 = User(pw='dizzy', name='박도라에몽', age='15', address='일산',birth='2007-3-12', gender='남자', create_date=datetime.now())
    a5 = User(pw='fool', name='박민수', age='22', address='대구', birth='2000-7-19', gender='남자', create_date=datetime.now())
    a6 = User(pw='gogo', name='최고심', age='25', address='제주',birth='1997-12-1', gender='여자', create_date=datetime.now())
    a7 = User(pw='hello', name='하나리', age='18', address='울산',birth='2004-10-20', gender='여자', create_date=datetime.now())
    a8 = User(pw='icecream', name='최명희', age='40', address='포항', birth='1982-11-8', gender='여자', create_date=datetime.now())
    a9 = User(pw='jelly', name='나미리', age='28', address='인천', birth='1994-4-10', gender='여자', create_date=datetime.now())
    a10 = User(pw='king', name='신짱아', age='17', address='영천', birth='2005-9-13', gender='여자', create_date=datetime.now())

    # db.session.add(a1);db.session.add(a2);db.session.add(a3);db.session.add(a4);db.session.add(a5)
    # db.session.add(a6);db.session.add(a7);db.session.add(a8);db.session.add(a9);db.session.add(a10)
    # db.session.commit()

    result=User.query.filter(User.age>=19).all()
    print('성인 유저들: ', result)

    result1 = User.query.filter(User.age < 20).all()
    print('미성년 유저들: ', result1)

    return 'Hello안녕, pybo!'
#함수 이름들 겹치지 않게 주의. hello_pybo 위에 썼으니 밑에는 x

@bp.route('/')
def index():
   return redirect(url_for('question._list'))

@bp.route('/webhook/', methods=['GET','POST'])
def webhook():
    print('웹훅') #이거나오면 이게 작동한다는 증거

    req=request.get_json()
    #print(req) #잘가져왔는지 확인용.
    if req['queryResult']['intent']['displayName'] == 'movie ranking':
        rankdata = Mrank()
        result = ''
        cnt = 1
        for temp in rankdata:
            result = result + str(cnt) + '위: ' + temp['title']+"\n "
            print(result)
            if cnt == 3:
                break
            cnt += 1
        return {'fulfillmentText':result}

    elif req['queryResult']['intent']['displayName'] == 'movie info - search':
        movie = navermovie(req['queryResult']['queryText']) #미나리라고 검색한 부분이 여기에 있음. 이걸 검색어로 navermovie함수에 넣어줌
        #print(movie) #잘가져왔는지 확인용.
        moviedata=movie['items'][0] #여기안에 우리가 필요한거 다있다. 젤 먼저 나오는 검색결과를 보여주려고 함.
        #return {'fulfillmentText': '제목:' + moviedata['title']+'감독: '+moviedata['director']+ '출연진: '+moviedata['actor']+ '연도: ' +moviedata['pubDate']}
        return movie_info(moviedata['image'], moviedata['title'], moviedata['link'],
                          '감독:' + moviedata['director'] + ' 출연자: ' + moviedata['actor'])
    elif req['queryResult']['intent']['displayName'] == 'weather info - city':
        #print(req) 정보가 어디서 들어오는지 확인
        weather=get_wdata(req['queryResult']['queryText'])
        #print(weather)
        return weather_info(weather)
    elif req['queryResult']['intent']['displayName'] == 'naver shopping - search':
        result = navershop(req['queryResult']['queryText'])
        items = result['items']
        item_list = []
        for item in items:
            title = item['title']
            link = item['link']
            image = item['image']
            lprice = item['lprice']
            hprice = item['hprice']
            if hprice == '':
                hprice = lprice
            item_dic = {'title': title, 'link': link, 'image': image, 'lprice': lprice, 'hprice': hprice}
            item_list.append(item_dic)
        return shop_info_with_links(item_list)

def shop_info_with_links(item_list):
    richContents = []
    for item in item_list:
        richContent = [
            { # 이 부분 지우면 그림이 안나옴
                "type": "image",
                "rawUrl": item['image']
            },
            { # 이 부분 지우면 정보가 안나옴
                "type": "info",
                "title": item['title'].replace('<b>','').replace('</b>',''),
                "actionLink": item['link'],
                "subtitle": '최저가:' + item['lprice'] + ' 최고가:' + item['hprice']
            }
        ]
        richContents.append(richContent)

    response_json = jsonify(
        fulfillment_text='네이버 쇼핑 상품 정보',
        fulfillment_messages=[
            {
                "payload": {
                    "richContent": richContents
                }
            }
        ]
    )
    return response_json

def weather_info(weather):
    strdata=''
    if '지역' in weather:
        strdata+= weather['지역'] + "의 "
    if '현재 일기' in weather and len(weather['현재 일기'])>1:
        strdata += "현재 일기예보는 " + weather['현재 일기'] + "이고"
    if '현재기온' in weather and len(weather['현재기온'])>1:
        strdata += "현재 기온은 " + weather['현재기온'] + "도, "
    if '일강수' in weather and len(weather['일강수'])>1:
        strdata+= "일 강수량은" + weather['일강수']
    strdata +=  "입니다."
    response_json = jsonify(
        fulfillment_text=strdata
    )
    return response_json

#def movie_ranking(imgurl, title, link, subtitle):


def movie_info(imgurl, title, link, subtitle):
    response_json = jsonify(
        fulfillment_text='영화바보',
        fulfillment_messages=[
            {
                "payload": {
                    "richContent": [[
                        {
                            "type": "image",
                            "rawUrl": imgurl
                        },
                        {
                            "type": "info",
                            "title": title,
                            "actionLink": link,
                            "subtitle": subtitle,
                        }
                    ]]
                }
            }
        ]
    )
    return response_json

############BTS vote##########
@bp.route('/btsvote', methods=['GET','POST'])
def btsvote():
    print('---------------------BTS vote---------------------')
    req = request.get_json()
    print(req)
    if req['queryResult']['intent']['displayName'] == 'BTS - vote':
        bts_member = req['queryResult']['parameters']['bts-member']

        voteresult=BTS_vote.query.get_or_404(bts_member)
        print(voteresult.count)
        voteresult.count+=1
        db.session.commit()

        strdata= str(bts_member)+"에게 투표하셨군요. 이용해주셔서 감사합니다!"
        response_json=jsonify(
            fullfillment_text=strdata
        )
        print('==========투표 결과: ', strdata)

    elif req['queryResult']['intent']['displayName'] == 'vote-ranking':
        vote_result = BTS_vote.query.order_by(BTS_vote.count.desc())
        strdata=''
        cnt=0

        for temp in vote_result:
            cnt+=1
            strdata=strdata+str(cnt)+'위: '+temp.name+' , 총 '+str(temp.count)+'표    | ' + '\n'
            if cnt ==3:
                break

        response_json = jsonify(
            fullfillment_text=strdata
        )
        return {'fulfillmentText': strdata}
    return response_json

@bp.route('/tt')
def tt():
    bts_list=['진','슈가','지민','V','RM','정국','J-hope']
    for b in bts_list:
        vote=BTS_vote(name=b, count=0)
        db.session.add(vote)

    db.session.commit()
    return redirect(url_for('main.index'))

