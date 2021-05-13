from datetime import datetime

from flask import Blueprint, render_template, request, url_for, flash, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from pybo.models import Question, pybo_User
from .. import db
from ..forms import QuestionForm, AnswerForm
from ..forms import UserCreateForm, UserLoginForm

bp=Blueprint('auth',__name__,url_prefix='/auth')
@bp.route('/signup',methods=('GET','POST'))
def signup():
    form=UserCreateForm()
    if request.method=='POST' and form.validate_on_submit:
        user=pybo_User.query.filter_by(username=form.username.data).first()
        if not user:
            user=pybo_User(username=form.username.data,
                           password=generate_password_hash(form.password1.data),
                           email=form.email.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('이미 존재하는 사용자입니다.')

    return render_template('auth/signup.html', form=form)

@bp.route('/login',methods=('GET','POST'))
def login():
    form=UserLoginForm()
    if request.method=='POST' and form.validate_on_submit():
        error=None
        user=pybo_User.query.filter_by(username=form.username.data).first()
        if not user:
            error='존재하지 않는 사용자입니다.'
        elif not check_password_hash(user.password,form.password.data):
            error='비밀번호가 올바르지 않습니다. '

        if error is None:
            session.clear()
            session['user_id']=user.id
            return redirect(url_for('main.index'))
        flash(error)

    return render_template('auth/login.html',form=form)

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = pybo_User.query.get(user_id)

@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.index'))