from flask import Blueprint, render_template
from utils import commonvalues as cv

pageController = Blueprint("pagecontroller", __name__)


@pageController.route('/', methods=[cv.GET])
def loadMain():
    return render_template("mypage.html")
