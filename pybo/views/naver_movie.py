from flask import Blueprint, url_for, render_template, request
from pybo.movieapi import Mrank
from pybo.Naver_API import naverbook
from pybo.forms import NaverBookForm
bp=Blueprint('movie', __name__, url_prefix='/movie')

@bp.route('/rank/')
def Movierank():
    rankdata= Mrank()

    return render_template('movie/movie_rank.html',ranklist=rankdata)
