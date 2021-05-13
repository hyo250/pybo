#미션_http://127.0.0.1/naver/movie를 입력하면 화면에 영화정보입니다. 뜨게 하기
from flask import Blueprint, url_for, render_template, request

from pybo.Naver_API import naverbook, navermovie
from pybo.forms import NaverBookForm
bp=Blueprint('naver', __name__, url_prefix='/naver')

@bp.route('/book/', methods=('GET','POST'))
def Naverbook():
    form=NaverBookForm()
    if request.method == "POST" and form.validate_on_submit():
       result= naverbook(form.search.data) #Naver_API의 naverbook
       return render_template('naver/naverbook.html', bookinfo_list=result['items'],form=form)

    return render_template('naver/naverbook.html', form=form)

@bp.route('/movie/', methods=('GET','POST'))
def Navermovie():
    form=NaverBookForm()
    if request.method == "POST" and form.validate_on_submit():
       result= navermovie(form.search.data) #Naver_API의 navermovie
       return render_template('naver/navermovie.html', movie_list=result['items'],form=form)

    return render_template('naver/navermovie.html', form=form)
