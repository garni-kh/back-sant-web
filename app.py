from flask import Flask
from flask_admin import Admin
from flasksql import ind12,CKTextAreaField
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView
from flask_wtf import FlaskForm
from wtforms import  FileField





app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+mysqlconnector://root:1332015@192.168.1.51/webprodact'


db = SQLAlchemy(app)


class IndustryPhotoForm(FlaskForm):
    photo = FileField('Industry Photo')

class Industries(ModelView):
        extra_js = ['//cdn.ckeditor.com/4.6.0/full-all/ckeditor.js']
        form_overrides = dict(testlong=CKTextAreaField)
        image_url = IndustryPhotoForm.photo
        column_list = ['id', 'Name',image_url]
       
        
      


admin = Admin(app, name='microblog', template_mode='bootstrap3')

admin.add_view(Industries(ind12, db.session))


app.run()
