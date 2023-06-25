""" this is tutorial codes"""
from flask import Flask, url_for, redirect, request, render_template, make_response, session, flash

app  = Flask(__name__)
app.secret_key = b'a5c841512d4b5bc989160f15106ad173'

@app.route("/")
def hello_world():
    """ test flask """
    print("thsi is my way")
    return 'hello'


def test_url():
    """ test url bind in route function """
    return "test url"

app.add_url_rule("/test","test",test_url)# the same route

@app.route("/test/<name>")
def test_dynamic_url(name):
    """ this is test dynamic url"""
    return "dynamic url " + name


@app.route("/canonical/<int:number>/")
def test_url2(number):
    """ test slash next url """
    return str(number)



@app.route("/testurlfor")
def test_urlfor():
    """ test url_for and status code"""

    #information 1xx
    #successful 2xx
    #redirection 3xx
    #client error 4xx
    #server error 5xx

    return redirect(url_for("hello_world"), code=200)


@app.route("/success/<name>")
def success(name):
    """ this is success"""
    return name + " is submit"


@app.route("/readcookie")
def get_cookie():
    """ It is for getting cookies"""
    print(request.cookies)
    #  #([('csrftoken', 'OLYOBGWs8F17fIkeITcGqEf3LKo68pzw'),
                            #('sessionid', '310woc711j1jyc13hwbwxlfnryts3y8g'), 
                            # ('userID', 'amirreza')])
    print(session)
    if 'username' in session:
        print(session['username'])
    
    session.pop('username', None)

    name = request.cookies.get("userID")
    
    return "Hello "+name


@app.route("/login", methods=['POST', 'GET'])
def login():
    """ this is for logging """
    if request.method == 'POST':
        flash("this is message")
        name = request.form['id_name']
        session['username'] = name
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie("userID", name)

        return resp
    else:
        return render_template("login.html")



@app.route("/grade/<int:grade>")
def level_define(grade):
    """ it is send parameter to html file """
    return render_template("grade.html", grade=grade)


@app.route("/use_for")
def use_for():
    """ it is test print dictionary in html file """
    dict_program = {"python":"yes", "java":"ok", "lisp":"no I am sorry"}
    return render_template("list_show.html", list_pro=dict_program)


@app.route("/upload", methods=['POST'])
def upload_file():
    """ upload file """
    
    #data = request.files['file'] # for upload file
    #data.save('img.png') #save uploaded file

    #read json post
    data = request.json
    print(data['user'])
    return data['user']

app.run(debug=True) #host, port, debug, options
