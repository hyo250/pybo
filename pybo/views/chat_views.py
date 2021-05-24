from datetime import datetime

from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

from pybo.models import Question
from .. import db
from ..forms import QuestionForm, AnswerForm, HelpForm
from pybo.dialogflowapi import chat

bp=Blueprint('chat', __name__,url_prefix='/chat')

@bp.route('/bot/')
def Bot():
    return render_template('chat/chatbot.html')

@bp.route('/help/', methods=('GET','POST'))
def Help():
    form=HelpForm()
    if request.method == "POST" and form.validate_on_submit():
        result = chat(form.search.data,'1234')  # chat_views.py의 함수 chat
        if result=='영화순위메뉴':
            return redirect(url_for('movie.Movierank'))
        elif result=='구글 검색':
            return redirect('http://www.google.com')


    return render_template('chat/help.html', form=form)

@bp.route('/vote/')
def vote():
    return render_template('chat/BTS_vote.html')
