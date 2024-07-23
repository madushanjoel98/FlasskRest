from flask import session


def setKeyd(token):
    session['jwt'] = token
