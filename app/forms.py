from flask_wtf import FlaskForm 
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	#login form. Asks for openid as string and a boolean remember me button. 
	openid=StringField('openid',validators=[DataRequired()])
	remember_me= BooleanField('remember_me',default=False)
