from django.db import models
from django.utils import timezone
from django.urls import reverse
import uuid

# Create your models here.
class Klass(models.Model):
	Klass = models.CharField(max_length=200)

	def __str__(self):
		return self.Klass

class Teacher(models.Model):
	Name = models.CharField(max_length=200)

	def __str__(self):

		return self.Name

class Country(models.Model):
	Country_Name = models.CharField(max_length=200)

	def __str__(self):

		return self.Country_Name

class District(models.Model):

	District_Name = models.CharField(max_length=200)

	def __str__(self):

		return self.District_Name

class Student(models.Model):

	First_Name = models.CharField(max_length=200)
	Last_Name = models.CharField(max_length=200)
	DOB = models.DateField(blank=True, null=True)
	Registration_Date = models.DateField()
	Guadian_Contact = models.CharField(max_length=200)
	Klass = models.ForeignKey('Klass',on_delete=models.CASCADE)
	District = models.ForeignKey('District',on_delete=models.CASCADE)
	Class_Teacher = models.ForeignKey('Teacher',on_delete=models.CASCADE)
	Citizenship = models.ForeignKey('Country',on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.First_Name},{self.Last_Name}'



class Genre(models.Model):

	name = models.CharField(max_length=200,help_text='Enter a book genre (e.g. Science Fiction)')

	def __str__(self):
		return self.name

class Book(models.Model):

	title = models.CharField(max_length=200)
	author = models.ForeignKey('Author',on_delete=models.CASCADE)
	summary = models.TextField(max_length=1000)
	isbn =  models.CharField('ISBN',max_length=13,help_text='Enter 13 character')
	genre = models.ManyToManyField(Genre,help_text='select genre for this book')

	def __str__(self):
		return self.title

	def get_absolute_url(self):

		return reverse('book-detail',args=[str(self.id)])

class BookIstance(models.Model):
	id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='Unique ID for this particular book across whole library')
	book = models.ForeignKey('Book',on_delete=models.CASCADE)
	imprint = models.CharField(max_length=200)
	due_back = models.DateField(null=True,blank=True)
	LOAN_STATUS = (

		('m','Maintenance'),
		('o','On loan'),
		('a','Available'),
		('r','Reserved'),

	)

	status = models.CharField(
		max_length=1,
		choices=LOAN_STATUS,
		blank=True,
		default='m',
		help_text='Book availability',

	)

	def __str__(self):
		return f'{self.id},({self.book.title})'


class Author(models.Model):
	First_Name = models.CharField(max_length=100)
	Last_Name = models.CharField(max_length=100)
	DOB = models.DateField(null=True,blank=True)
	DOD = models.DateField('Died',null=True,blank=True)

	def __str__(self):
		return f'{self.First_Name},{self.Last_Name}'

	def get_absolute_url(self):

		return reverse('author-detail',args=[str(self.id)])