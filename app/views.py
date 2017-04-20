from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


@app.route('/login',methods = ['GET','POST'])

def login():
    #create form for user to post username 
    form = 	LoginForm()
    #only proceed to index page if login was successful. 
    if form.validate_on_submit():
    	flash('Login requested for OpenId="%s". remember_me set to %s' % (form.openid.data,str(form.remember_me.data)))
    	return redirect('/index')


    #else, render the login page.	
    return render_template('login.html',title='Sign_In',form=form, providers=app.config['OPENID_PROVIDERS'])

@app.route('/index',methods = ['GET','POST'])

def index():
	user = {'nickname':'Jerry'}
	posts = [{'author':{'nickname':'Jerry'},'body':'is awesome'}]
	return render_template('index.html',title = 'Home',user=user,posts=posts)    