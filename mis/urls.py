from django.urls import path
from mis import views

urlpatterns = [

	path('',views.index,name='index'),
	path('book/<int:pk>',views.BookDetailView.as_view(),name='book-detail'),
	path('books',views.BookListView.as_view(),name='books'),
	path('author/<int:pk>',views.AuthorDetailView.as_view(),name='author-detail'),
	path('authors',views.AuthorListView.as_view(),name='authors'),

]