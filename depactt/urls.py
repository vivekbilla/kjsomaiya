from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-login', views.login, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-login'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-signup', views.signup, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-signup'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-adminsignup', views.adminsignup, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-adminsignup'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-admincode', views.admincode, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-admincode'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-home', views.home, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-home'),
    # ex: /polls/5/
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-profile', views.profile, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-profile'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-help', views.help, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-help'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-addevent', views.addevent, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-addevent'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-allevents', views.allevents, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-allevents'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-upcomingevents', views.upcomingevents, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-upcomingevents'),
    path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-finishedevents', views.finishedevents, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-finishedevents'),

    path('alldel',views.alldel, name='alldel'),
    path('homelogout',views.homelogout, name='homelogout'),
    path('addeventlogout',views.addeventlogout, name='addeventlogout'),
    path('alleventlogout',views.alleventlogout, name='alleventlogout'),
    path('upcominglogout',views.upcominglogout, name='upcominglogout'),
    path('finishedlogout',views.finishedlogout, name='finishedlogout'),
    path('profilelogout',views.profilelogout, name='profilelogout'),
    path('helplogout',views.helplogout, name='helplogout')

]




#     path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-allevents', views.allevents, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-allevents'),
#     path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-upcomingevents', views.upcomingevents, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-upcomingevents'),
#     path('kjsomaiyacollegeofengineeringandinformationtechnologyteachers-finishedevents', views.finishedevents, name='kjsomaiyacollegeofengineeringandinformationtechnologyteachers-finishedevents'),
