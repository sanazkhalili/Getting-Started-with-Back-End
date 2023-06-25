""" this is for connecting and reading data from mysql with sqlalchemy"""
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:sanaz11@192.168.120.192:3306/captcha'
app.config['SECRET_KEY'] = "e0f2ecbb442dcb6588c060ba8c112641"

db = SQLAlchemy(app)

class CreateGoal(db.Model):
    """ this use from database"""
    id = db.Column(db.Integer, primary_key=True)
    goal_name = db.Column(db.String(20))
    description = db.Column(db.String(100))


with app.app_context ():
    db.create_all ()


@app.route("/create")
def create():
    """ this is for add a goal to table goal"""
    data = request.json
    new_goal = CreateGoal(goal_name=data['name'], description=data['desc'])
    db.session.add(new_goal)
    db.session.commit()
    return "saved"

@app.route("/get_goal")
def get():
    """ get goals """
    goals = CreateGoal.query.all()
    return render_template("goal_list.html", lists = goals)

app.run()
