from flask import Flask

app=Flask(__name__)

#url : http://www.naver.com/webtoon/  플라스크로 크롤링하면 naver.com/까지 됨.

#주소를 만드는 방법. @(데코레이터) 이용.

#http://naver.com/

@app.route('/') #route=url임.
def hello_pybo():
    return '하이~ HI~ 플라스크~ FLASK~'
#플라스크는 무조건 터미널창에서 코드실행!
#FLASK_APP 수동설정.(자동도 됨)
#set FLASK_APP=내가 실행할 파일 이름 ==>> 터미널창에 입력. #한번만 실행
#set FLASK_ENV=development => 디버그 활성화 #한번만 실행
#flask run #컨트롤씨와 함께 껐다켰다하기.
#http://127.0.0.1:5000/ 포트번호가 5000

#주소/news '뉴스화면입니다.' 로 만들기
@app.route('/news')
def news():
    return '뉴스입니다.'

@app.route('/weather')
def weather():
    return '날씨 보여줄까요?'

@app.route('/music')
def music():
    return '오늘의 추천 음악입니다.'