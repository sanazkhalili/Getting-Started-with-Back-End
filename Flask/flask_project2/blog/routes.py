from blog import app, db, bcrypt
from flask import render_template, redirect, url_for, flash, request
from .forms import RegisterForm, CreatePostForm
from .models import User, Post
from .models import db as database
from flask import g

test = 1002


with app.app_context():
    database.create_all()

@app.before_request
def create_g():
    print('in_create_g')
    g.value = 1222
    g.value = g.get('value')+1

@app.route("/test_g")
def test_g():
    print(g.get('value')+1)
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """ this is a function for user register """
    register_form = RegisterForm()

    if request.method == 'POST':
        if register_form.validate_on_submit():
            hash_pass = bcrypt.generate_password_hash(register_form.password.data).decode('utf-8')
            new_user = User(username=register_form.username.data, 
                            password=hash_pass, email=register_form.email.data)

            db.session.add(new_user)
            db.session.commit()
            flash("You register successfully", category="success")
            return redirect(url_for('home'))
        else:
            flash("It isn't validation data", category="error")
    return render_template('register.html', form=register_form)


@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    post_form = CreatePostForm()

    if request.method=='POST':
        
        if post_form.validate_on_submit():
            new_post = Post(title=post_form.title.data,
                            content = post_form.content.data, date='2020-02-03', user_id=1)
            db.session.add(new_post)
            db.session.commit()
            flash("Your post saved successfully", category="success")
            return redirect(url_for('home'))
        else:
            return post_form.errors
    elif request.method=='GET':
        return render_template('post.html', form=post_form)
