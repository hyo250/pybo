from datetime import datetime

from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

from pybo.models import Question
from .. import db
from ..forms import QuestionForm, AnswerForm


bp=Blueprint('chat', __name__,url_prefix='/chat')

@bp.route('/bot/')
def Bot():
    return render_template('chat/chatbot.html')