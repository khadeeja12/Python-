from flask import *
from database import *

admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():

	return render_template('adminhome.html')


@admin.route('/category',methods=['post','get'])	
def category():
	data={}
	if "add" in request.form:
		catnm=request.form['catname']
		catdes=request.form['catdesc']
		q="insert into category values(null,'%s','%s')"%(catnm,catdes)
		insert(q)
	s="select * from category"
	res=select(s)
	data['cat']=res
	return render_template('category.html',data=data)
	     
