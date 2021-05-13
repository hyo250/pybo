import os

BASE_DIR=os.path.dirname(__file__) #현재 이 파일이 있는 경로를 가져와라 '__file__'

#sqlarchemy 이용한 데이터베이스 주소 설정.
SQLALCHEMY_DATABASE_URI= 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS=False #기본적으로 false

SECRET_KEY="dev"