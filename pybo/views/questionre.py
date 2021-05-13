from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

from pybo.models import Question

#127.0.0.1:5000/question/list
#127.0.0.1:5000/question/detail/3

bp=Blueprint('questionre', __name__,url_prefix='/questionre')

@bp.route('/list/')
def _list():
    return redirect(url_for('question._list'))
