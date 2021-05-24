from pybo import db #iniy__py에 들어있는 변수 db를 가져와라

class Question(db.Model): #질문을 등록할 수 있는 테이블 생성
    id=db.Column(db.Integer,primary_key=True) #이 테이블에 id라는 컬럼을 만들고,  int형 데이터 넣어라.
    subject =db.Column(db.String(200),nullable=False) #200글자로 제한. nullable= 비어두기 허용 유무..
    content=db.Column(db.Text(), nullable=False)
    create_date=db.Column(db.DateTime(), nullable=False)

class Answer(db.Model):
    id=db.Column(db.Integer,primary_key=True) #primary_key는 고윳값. 주민등록같은거
    question_id=db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE')) #ForeignKey 다른 테이블의 pk(primary key)값을 쓸때 여기서는 foreignkey라고 함. ondelete= 원래 것이 삭제디면 여기서도 삭제되라. 연동의 의미..
    question=db.relationship('Question', backref=db.backref('answer_set')) #참조 #backref는 역참조. relationship은 묶어주는 역할
    content=db.Column(db.Text(),nullable=False)
    create_date=db.Column(db.DateTime(),nullable=False)

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    pw = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    address=db.Column(db.String(40), nullable=False)
    birth=db.Column(db.String(20), nullable=False)
    gender=db.Column(db.String(2), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


class pybo_User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(150), unique=True, nullable=False)
    password=db.Column(db.String(200), nullable=False)
    email=db.Column(db.String(120),unique=True, nullable=False)

class BTS_vote(db.Model):
    name=db.Column(db.String(100), primary_key=True)
    count=db.Column(db.Integer, nullable=False)