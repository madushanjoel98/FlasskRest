from flask import Blueprint, jsonify, request
from utils import commonvalues as cv
import models.CommonResponseModel as respm
from logics.readerCSV import CSVReader
import dao.usertableDAO as usdao
from utils.LOG import logger as dev

userController = Blueprint("usercontroller", __name__)


@userController.route('/uploadCsv', methods=[cv.POST])
def upload_file():
    res = None
    stCode = cv.SUCCESS_CODE;
    try:
        dataform = request.form
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        if file:
            csv_reader = CSVReader(file)
            base = csv_reader.get_base64_chart(x_value=dataform.get("x_value"), y_value=dataform.get("y_value"),
                                               kind=dataform.get("kind"))
            res = respm.CommonRequestModel(message="Success", data={"base": base}, code=1)
    except Exception as e:
        stCode = cv.NOTFOUND_CODE
        res = respm.CommonRequestModel(message=f"Fail {e}", data=None, code=2)
    return jsonify(res.createDictionarie()), stCode


@userController.route("/getv", methods=[cv.POST])
def getFromDB():
    rws = None
    try:
        dev.info(msg="getV")
        rws = respm.CommonRequestModel(message="Success", data=usdao.getAllUsers(), stcodes=200,
                                       code=1).createDictionari_respo()
    except Exception as e:
        rws = respm.CommonRequestModel(message=f"Fail {e}", data=None, stcodes=400, code=1).createDictionari_respo()

    return rws


@userController.route("/getbyid", methods=[cv.POST])
def getFromDBgetbyid():
    rws = None
    try:
        rqdaa = request.get_json()
        print(rqdaa)
        rws = respm.CommonRequestModel(message="Success", data=usdao.getAllUsersByEPF(rqdaa["epf"]), stcodes=200,
                                       code=1).createDictionari_respo()
    except Exception as e:
        rws = respm.CommonRequestModel(message=f"Fail {e}", data=None, stcodes=400, code=1).createDictionari_respo()

    return rws


@userController.route("/getbyname", methods=[cv.POST])
def getFromDBgetbyName():
    rws = None
    try:
        rqdaa = request.get_json()
        print(rqdaa)
        rws = respm.CommonRequestModel(message="Success", data=usdao.getAllUsersByName(rqdaa["name"]), stcodes=200,
                                       code=1).createDictionari_respo()
    except Exception as e:
        rws = respm.CommonRequestModel(message=f"Fail {e}", data=None, stcodes=400, code=1).createDictionari_respo()

    return rws


@userController.route("/login", methods=[cv.POST])
def getFromDBLogin():
    rws = None
    try:
        rqdaa = request.get_json()
        mof = usdao.login(username=rqdaa["username"], password=rqdaa["password"])
        rws = respm.CommonRequestModel(message="Success", data=mof, stcodes=200,
                                       code=1).createDictionari_respo()
    except Exception as e:
        rws = respm.CommonRequestModel(message=f"Fail {e}", data=None, stcodes=400, code=1).createDictionari_respo()

    return rws
