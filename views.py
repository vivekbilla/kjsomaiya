from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.template import loader

# from .models import Question
from django.contrib.auth.models import User, auth
# from .forms import Form

# from .models import Signup
from .models import Event

from json import dumps
import psycopg2
from datetime import datetime



def index(request): 
    # create data dictionary 
    # dump data 

    return render(request, 'depactt/index.html')


def login(request): 
	# create data dictionary 
	# dump data 
	if request.method=='POST':
		uname=request.POST['usname']
		passwordrr1=request.POST['pssword']

		if (len(uname)==0) or(len(passwordrr1)==0):
			return redirect('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-login')
		else:
			user = auth.authenticate(username=uname, password=passwordrr1)
			if user is not None:
				print('it worked')
				auth.login(request, user)
				# return user
				return redirect('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-home')
			else:
				print('user doesnt exists or password wrong');
				return redirect('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-login')
	else:
		return render(request, 'depactt/login.html')

def home(request): 

	return render(request, 'depactt/home.html')


def profile(request): 

	return render(request, 'depactt/profile.html')


def help(request): 

	return render(request, 'depactt/help.html')

def allevents(request): 
    # create data dictionary 
    # dump data 
    events=Event.objects.all()
    dicevents = {
    	"event_number": events
    }
    return render(request, 'depactt/allevents.html',dicevents)

def finishedevents(request): 
    # create data dictionary 
    # dump data 
    events=Event.objects.filter(eventfinished=True)
    dicevents = {
    	"event_number": events
    }
    return render(request, 'depactt/finishedevents.html',dicevents)

def upcomingevents(request): 
    # create data dictionary 
    # dump data 
    events=Event.objects.filter(eventfinished=False)
    dicevents = {
    	"event_number": events
    }
    return render(request, 'depactt/upcomingevents.html',dicevents)

def addevent(request):
	if request.method=='POST':
		eventname=request.POST['eventname']
		eventorgc=request.POST['eventcommittee']
		eventdescription=request.POST['eventdesc']
		eventda=request.POST['eventdate']
		eventorg1=request.POST['eventorganizer1']
		eventorg2=request.POST['eventorganizer2']
		eventorg3=request.POST['eventorganizer3']
		eventcon1=request.POST['eventconvener1']
		eventcon2=request.POST['eventconvener2']
		eventfin=request.POST.get('eventfinished',False)
		eventdep=request.POST['eventdepartment']
		publishdate=request.POST['pubdate']
		ecom=request.POST['com']
		# user = auth.authenticate(username=uname, password=passwordrr1)
		if Event.objects.filter(eventtitle=eventname).exists():
			print('event exists');
			return redirect('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-addevent')
		else:
			# sql = """INSERT INTO Event(event_title,event_organizer,event_description,event_poster,event_date,event_organizing_teacher1,event_organizing_teacher2,event_organizing_teacher3,event_organizing_convener1,event_organizing_convener2,event_finished,event_department) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING vendor_id;"""
			# eventt=(eventname,eventorgc,eventdescription, eventpos, eventda, eventorg1, eventorg2, eventorg3, eventcon1, eventcon2, eventfin, eventdep)

			eventt= Event(eventtitle=eventname, eventorganizer=eventorgc, eventdescription=eventdescription, eventdate=eventda, eventteacher1=eventorg1, eventteacher2=eventorg2, eventteacher3=eventorg3, eventconvener1=eventcon1, eventconvener2=eventcon2, eventfinished=eventfin, eventdepartment=eventdep, pubdate=publishdate, eventcomments=ecom)
			eventt.save();
			# cursor.execute(sql, eventt)
			print('event doesnt exists or password wrong');

			return redirect('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-addevent')

	else:
		return render(request,'depactt/addevent.html')


# def home(request): 

# 	return render(request, 'depactt/home.html')


# def home(request): 

# 	return render(request, 'depactt/home.html')

def signup(request):
	if request.method=='POST':
		fname=request.POST['firstname']
		lname=request.POST['lastname']
		ename=request.POST['emailid']
		uname=request.POST['username']
		passwordrr1=request.POST['password1']
		passwordrr2=request.POST['password2']

		if (len(fname)==0) or(len(lname)==0) or(len(ename)==0) or(len(uname)==0) or(len(passwordrr1)==0) or(len(passwordrr2)==0):
			return redirect('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-signup')
		else:
			if passwordrr1==passwordrr2:
				if User.objects.filter(username=uname).exists():
					print('user exists');
					return redirect('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-signup')
				else:
					user= User.objects.create_user(username=uname, first_name=fname, last_name=lname, email=ename, password=passwordrr1)
					user.save();
					print('it worked');
					return redirect('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-home')
			else: 
				return redirect('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-signup')

	else:
		return render(request,'depactt/signup.html')


def admincode(request): 

	return render(request, 'depactt/admincode.html')

def adminsignup(request):
	if request.method=='POST':
		fname=request.POST['firstname']
		lname=request.POST['lastname']
		ename=request.POST['emailid']
		uname=request.POST['username']
		passwordrr1=request.POST['password1']
		passwordrr2=request.POST['password2']

		if (len(fname)==0) or(len(lname)==0) or(len(ename)==0) or(len(uname)==0) or(len(passwordrr1)==0) or(len(passwordrr2)==0):
			print('kya dude')
			return redirect('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-adminsignup')
		else:
			if passwordrr1==passwordrr2:
				if User.objects.filter(username=uname).exists():
					print('user exists');
					return redirect('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-adminsignup')
				else:
					user= User.objects.create_superuser(username=uname, first_name=fname, last_name=lname, email=ename, password=passwordrr1)
					user.save();
					print('it worked');
					return redirect('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-home')
			else: 
				return redirect('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-adminsignup')

	else:
		return render(request,'depactt/adminsignup.html')


def addeventlogout(request):
	auth.logout(request)
	return redirect('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-addevent')


def homelogout(request):
	auth.logout(request)
	return redirect('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-home')

def upcominglogout(request):
	auth.logout(request)
	return redirect('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-upcoming')

def finishedlogout(request):
	auth.logout(request)
	return redirect('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-finished')

def alleventlogout(request):
	auth.logout(request)
	return redirect('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-allevent')

def profilelogout(request):
	auth.logout(request)
	return redirect('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-profile')

def helplogout(request):
	auth.logout(request)
	return redirect('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-help')



def alldel(request):
	if request.method == "POST":
		print('entered post')
		evid=request.POST.get("dell", "")
		print(evid)
		Event.objects.filter(id=evid).delete()
		return redirect('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-allevents')
	else:
		return redirect('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-allevents')