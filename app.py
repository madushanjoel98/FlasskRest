from flask import Flask
from flask_jwt_extended import JWTManager
from routes.UserRoute import userController
from routes.loginController import loginController
from renderpages.PageController import pageController
from utils.database import db_session, init_db
from utils.connections import MYConnection
import uuid
from utils.Config import Config

app = Flask(__name__)
app.config.from_object(Config)

# engine = create_engine("mysql+pymysql://user:pass@some_mariadb/dbname?charset=utf8mb4")
app.register_blueprint(userController, url_prefix="/usercontroller")
app.register_blueprint(loginController, url_prefix="/my")
app.register_blueprint(pageController, url_prefix="/page")
connecDB = MYConnection()

jwt = JWTManager(app=app)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    init_db()
    print(uuid.uuid4())
    connecDB.get_connection().connect()
    app.run(debug=True)
