from datetime import datetime

from flask import Blueprint, render_template, url_for,request

from pybo import db
from pybo.forms import AnswerForm
from pybo.models import Question,Answer
from werkzeug.utils import redirect

#127.0.0.1:5000/question/list
#127.0.0.1:5000/question/detail/3

bp=Blueprint('answer', __name__,url_prefix='/answer')

@bp.route('/create/<int:question_id>',methods=('POST', ))
def create(question_id): #()안에 인자값 필수. 몇번에 대한 답인지를 표시해야. int뒤의 것과 동일.
    #form.py 수정 후
    form=AnswerForm()
    question = Question.query.get_or_404(question_id)

    if form.validate_on_submit(): #form에 오류없으면 아래 코드실행해서 등록시켜라.
        #print(request)

        content=request.form['content']
        #answer=Answer(content=content, create_date=datetime.now())
        #방법1)
        # question.answer_set.append(answer)
        # db.session.commit()
        #방법2)
        answer=Answer(question=question, content=content, create_date=datetime.now())
        db.session.add(answer)
        db.session.commit()

        return redirect(url_for('question.detail',question_id=question_id))
    return render_template('question/detail.html', question=question, form=form) #form에 문제있으면 다시 질문페이지가 뜨게 해라 .