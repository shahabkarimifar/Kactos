from django.shortcuts import render

from .models import Genre, Book
from users.models import CustomUser


def home(request):

	data = dict()
	data['genres'] = Genre.objects
	data['suggests'] = Book.objects.filter(suggest=True)
	data['number_of_books'] = Book.objects.count()
	data['number_of_users'] = CustomUser.objects.count()

	return render(request, 'home.html', data)
