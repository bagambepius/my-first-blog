from django.shortcuts import render
from .models import Student,Book,Author,BookIstance
from django.views import generic

# Create your views here.

def index(request):

	total_no_of_students = Student.objects.all().count()
	total_no_of_books = Book.objects.all().count()
	#number of authors
	total_no_of_authors = Author.objects.all().count()
	total_no_of_Instances = BookIstance.objects.all().count()
	total_no_of_Instances_available = BookIstance.objects.filter(status__exact='a').count()
	#vist counts tracking using sessions as below

	vist_num = request.session.get('vist_num',0)
	request.session['vist_num'] = vist_num + 1

	context = {

		'total_no_of_students':total_no_of_students,
		'total_no_of_books':total_no_of_books,
		'total_no_of_authors':total_no_of_authors,
		'total_no_of_Instances':total_no_of_Instances,
		'total_no_of_Instances_available':total_no_of_Instances_available,
		'vist_num':vist_num,
	}
	return render(request,'index.html',context=context)

class BookDetailView(generic.DetailView):

	model = Book


class BookListView(generic.ListView):
	model = Book


class AuthorDetailView(generic.DetailView):
	model=Author

class AuthorListView(generic.ListView):
	model=Author