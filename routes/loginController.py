from flask import Blueprint, jsonify, request
from utils import commonvalues as cv
import models.CommonResponseModel as respm
from models.UserModel import User
from mypack.encryption import i_encrypt, i_decrypt
import logging as LOG
from utils.database import db_session
from flask_jwt_extended import jwt_required

loginController = Blueprint("logincontroller", __name__)


@loginController.route('/signup', methods=[cv.POST])
def signupUser():
    data = request.get_json()
    res = None
    stCode = cv.SUCCESS_CODE
    try:
        use = User(name=data["name"], email=data["email"], password=data["password"])
        db_session.add(use)
        db_session.commit()
        res = respm.CommonRequestModel(message="Success", data=use.to_dict(), code=1)
    except Exception as e:
        stCode = cv.NOTFOUND_CODE
        res = respm.CommonRequestModel(message=f"Failed {e}", data=None, code=2)

    return jsonify(res.createDictionarie()), stCode


@loginController.route('/encryption', methods=[cv.POST])
@jwt_required()
def encryption():
    stCode = 200

    try:
        data = request.get_json()
        key = data["key"]
        text = data["text"]
        responser = {
            "text": i_encrypt(text=text, secret_key=key)
        }
        res = respm.CommonRequestModel(message="Success", data=responser, code=1)
    except Exception as e:
        stCode = 400
        res = respm.CommonRequestModel(message=f"Error {e}", data=None, code=1)
    return jsonify(res.createDictionarie()), stCode


@loginController.route('/decryption', methods=[cv.POST])
def decryptionx():
    stCode = 200

    try:
        LOG.info(msg="decrypting message")
        data = request.get_json()
        key = data["key"]
        text = data["text"]
        responser = {
            "text": i_decrypt(encrypted_text=text, secret_key=key)
        }
        res = respm.CommonRequestModel(message="Success", data=responser, code=1)
    except Exception as e:
        LOG.error(msg=f"Fail to Decrypt due to {e}")
        stCode = 400
        res = respm.CommonRequestModel(message=f"Error {e}", data=None, code=1)
    return jsonify(res.createDictionarie()), stCode
