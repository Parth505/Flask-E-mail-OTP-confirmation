from flask import Flask , render_template , request, url_for, redirect
from flask_mail import Mail , Message 
from random import randint
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField , IntegerField

app=Flask(__name__)

otp=randint(000000,999999)

app.config['SECRET_KEY']  = 'secretKey'

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'parthsethi85@gmail.com'
app.config['MAIL_PASSWORD'] = 'email_id_password_here'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

class E_mailForm(FlaskForm):
	email = StringField('Email')
	submit = SubmitField('Verify')

class validationForm(FlaskForm):
	OTP  = IntegerField('Enter recived OTP')
	submit = SubmitField('Verify')


       





@app.route('/',methods=['GET','POST'])
def index():
	form = E_mailForm()
	if form.validate_on_submit():
		#email = form.email.data
		email=request.form['email']
		msg  = Message('Confirm Mail',sender='parthsethi85@gmail.com',recipients=[email])
		msg.body='Your OTP is ' + str(otp)
		mail.send(msg)
		return redirect(url_for('validate'))

	return render_template('index.html',form=form)



@app.route('/validate',methods=['GET','POST'])
def validate():
	form = validationForm()
	if form.validate_on_submit() and form.OTP.data == int(otp):
		return 'correct'
	return render_template ('check.html',form=form)




#@app.route('/validate',methods=['GET','POST'])
#def validate():
	#form = validationForm()   user_otp=request.form['otp']
#	form = validationForm()
	#user_otp=form.OTP.data
#	if form.validate_on_submit():
#		user_otp=form.OTP.data
#		if user_otp == int(otp):
#			return 'done'
#		else:
#			return 'not done'
#	return render_template('check.html')


		
	
    #user_otp=request.form['otp']
   # user_otp = form.OTP.data
    #if otp==int(user_otp):
 #       return "<h3>Email varification succesfull</h3>"







	#email=request.form['email']
	#msg=Message('test',sender='parthsethi85@gmail.com',recipients=[email])
	#msg.body = ' test e mail, dont reply'
	#msg.body=str(otp)
	#mail.send(msg)
	#return render_template('index.html')
	#return 'send'




if __name__=='__main__':
	app.run(debug=True)




