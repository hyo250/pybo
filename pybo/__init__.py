from flask import Flask

#config 파일 등록
from flask_migrate import Migrate #migrate 자동으로 테이블 생성의..
from flask_sqlalchemy import SQLAlchemy
import config

db=SQLAlchemy()
migrate= Migrate()


app= Flask(__name__)

#sqlalcehmy db 설정. 순서 중요.
#1)
app.config.from_object(config) #config 연결
db.init_app(app)
migrate.init_app(app,db)
#2)
from . import models
#3)
from .views import main_views, naver_views, question_views, answer_views, auth_views, naver_movie
app.register_blueprint(main_views.bp) #앱에다 등록시키는 이 과정이 있어야 함.
app.register_blueprint(naver_views.bp) #naver.py에서도 bp=Blureprint라고 변수정의했어서 .bp
app.register_blueprint(question_views.bp)
app.register_blueprint(answer_views.bp)
app.register_blueprint(auth_views.bp)
app.register_blueprint(naver_movie.bp)

from .filter import format_datetime
app.jinja_env.filters['datetime']=format_datetime

#플라스크로 웹서버만들때. 패키지 만들기(파이썬 폴더 패키지) 후 views(디렉토리)

#SQL쿼리문으로 데이터베이스 관리하는 시스템(?), NO-SQL
#sql: mysql, orcle, mariaDB, MS-sql, SQLite(파이썬 내장됨)
#no-sql:몽고db, redis, ... 쿼리문을 쓰지 않고 사용함.

#pip install Flask-Migrate 설치완료!

#내가 사용할 데이터베이스 입력하기(config. myproject 폴더 아래임 주의. )

