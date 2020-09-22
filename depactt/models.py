from django.db import models

# Create your models here.

class Event(models.Model):
	eventtitle = models.CharField(max_length=200)
	eventdescription = models.TextField()
	eventposter = models.ImageField(upload_to='posters', blank=True)
	eventdate = models.DateTimeField('date of event')
	eventorganizer = models.TextField()
	eventteacher1 = models.CharField(max_length=200)
	eventteacher2 = models.CharField(max_length=200)
	eventteacher3 = models.CharField(max_length=200, blank=True)
	eventconvener1 = models.CharField(max_length=200)
	eventconvener2 = models.CharField(max_length=200)
	eventdepartment = models.CharField(max_length=200, blank=True)
	eventfinished = models.BooleanField(default=False)
	pubdate = models.DateTimeField('date published')
	eventcomments = models.TextField(blank=True)