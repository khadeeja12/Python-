from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/')
def home():
	return render_template('home.html')

@public.route('/login',methods=['post','get'])	     
def login():
	if "login" in request.form:
		u=request.form['uname']
		p=request.form['pwd']
		print(u,p)
		a="select * from login where username='%s' and password='%s'"%(u,p)
		print(a)
		res=select(a)
		if res:
			if res[0]['user_type']=='admin':
				return redirect(url_for('admin.adminhome'))
	return render_template('login.html')

@public.route('/register',methods=['post','get'])	
def register():
	if "register" in request.form:
		fnm=request.form['fname']
		lnm=request.form['lname']
		gender=request.form['gender']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		district=request.form['district']
		uname=request.form['uname']
		password=request.form['password']
		print(fnm,lnm,gender,place,phone,email,district,uname,password)
		q="insert into login values(null,'%s','%s','user')"%(uname,password)
		id=insert(q)
		q="insert into registration values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(id,fnm,lnm,gender,place,phone,email,district)
		insert(q)
	return render_template('register.html')
