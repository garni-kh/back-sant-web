

from flask_sqlalchemy import SQLAlchemy



from wtforms import TextAreaField
from wtforms.widgets import TextArea


db = SQLAlchemy()

class fileTDS1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64))
    description =db.Column(db.String(500))
    path = db.Column(db.Unicode(128))

    def __unicode__(self):
        return self.name

class fileIMage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64))
    description =db.Column(db.String(500))
    path = db.Column(db.Unicode(128))

    def __unicode__(self):
        return self.name

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,backref=db.backref('users', lazy='dynamic'))

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return (self.id)
  #  def check_password(self, password):
   #     return check_password(password)
    #def set_password(self, password):
     #   self.pwdhash = generate_password_hash(password)



class ind12(db.Model):

    __tablename__='ind'
    id = db.Column(db.Integer, primary_key=True)
    Name=db.Column(db.String(250))
    text=db.Column(db.TEXT)
    URL=db.Column(db.String(250))
    testlong=db.Column(db.TEXT)
    url1=db.Column(db.String(300))
    #prodID=db.relationship('ind', backref='ind',lazy='dynamic')
    def __repr__(self):
        return '%s' % (self.Name)



class prodacts12(db.Model):
    __tablename__= 'prodacts'
    ID = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(350))
    #categories = db.relationship('Category', secondary=category_candidat,
                        #         backref=db.backref('candidat', lazy='dynamic'))
    name = db.Column(db.String(200))
    title = db.Column(db.TEXT)
    URL = db.Column(db.String(350))
    picurl = db.Column(db.String(350))
    text = db.Column(db.TEXT)
    telegrampicurl=db.Column(db.String(350))

class userForm(db.Model):
    __tablename__='litform'
    id=db.Column(db.Integer,primary_key=True)
    Name=db.Column(db.String(100))
    email=db.Column(db.String(150))
    mobile=db.Column(db.String(50))
    ostan=db.Column(db.String(50))
    sub=db.Column(db.String(100))
    text=db.Column(db.TEXT)
    direct=db.Column(db.String(60))

class blogNews(db.Model):
    __tablename__="news"
    ID=db.Column(db.Integer,primary_key=True)
    textblog=db.Column(db.TEXT)
    title=db.Column(db.String(250))
    subject=db.Column(db.String(250))
    autor=db.Column(db.String(250))
    date1=db.Column(db.String(20))
    category=db.Column(db.String(100))

class solotion12(db.Model):
    __tablename__="solotion"
    ID=db.Column(db.Integer,primary_key=True)
    ind_category=db.Column(db.String(350))
    solotion_name=db.Column(db.String(100))
    text=db.Column(db.TEXT)
    url=db.Column(db.String(350))


class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)

class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()




