from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin


app = Flask(__name__)
app.config['SECRET_KEY'] = '7693bcbca1a8c0af7e53eb55e077fa66'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:sanaz11@localhost:3306/captcha'
db = SQLAlchemy(app)


bcrypt = Bcrypt(app)




from blog import routes