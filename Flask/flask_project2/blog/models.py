from blog import db
import datetime
from flask_login import UserMixin

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    # در جدول فیلدی به نام پست ذخیره نمی شود
    # منظور مدل پست است
    # backref برای دسترسی از یوزر به پست هایش هست
    # lazy به معنای آن است که تا زمانی که مجبور نشده کاری انجام ندهد

    def __reper__(self): #for programming
        return f'{self.__class__.__name__}({self.email})'
    
    def __str__(self):# for user
        pass

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 
    # دلیل کوچک نوشتن حروف جدول این است که با مدلش کار نمی کنیم با نام جدول کار می کنیم


    def __reper__(self):
        return f'{self.__class__.__name__}({self.title[:30]})' #Post({self.title[:30]})



'''
u1 = User(username='', email='', password='')
db.session.add(u1)
db.session.commit()
p1 = Post(title="title1", content="contentttttt", author=u1)

all_post = Post.query.all()
user1 = User.query.first()

user1.posts # پست های آن یوزر را بر می گرداند
'''
