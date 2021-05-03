from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from myweb.models import Resume,User
from django.contrib import messages

# Create your views here.
def index(request):

	res1 = Resume()
	res1.name = "Python"
	res1.des = "Programming"
	res1.img = "c.jpg"

	res2 = Resume()
	res2.name = "C/C++"
	res2.des = "Programming"
	res2.img = "comp.jpg"

	res3 = Resume()
	res3.name = "D'jango"
	res3.des = "Framework"
	res3.img = "django.jpg"

	res4 = Resume()
	res4.name = "Data Anlysis"
	res4.des = "Analysis"
	res4.img = "ana.jpg"

	res5 = Resume()
	res5.name = "Web Development"
	res5.des = "Development"
	res5.img = "web.jpg"

	res6 = Resume()
	res6.name = "Machine Learning"
	res6.des = "Data Science"
	res6.img = "ML.png"
 
	response = [res1,res2,res3,res4,res5,res6]
 
	if request.method == "POST":
		First_Name = request.POST.get('First_Name')
		Last_Name = request.POST.get('Last_Name')
		Email = request.POST.get('Email')
		Phone = request.POST.get('Phone')
		message = request.POST.get('message')
  
		user = User(First_Name=First_Name,Last_Name=Last_Name,Email=Email,Phone=Phone,message=message , date = datetime.today())
  
		user.save()

		messages.success(request, 'Your Message has been sent.')
	return render(request,'index.html',{'response':response})