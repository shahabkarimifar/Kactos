from django.shortcuts import render, redirect
from django.http import HttpRequest
from magic import from_file as check_file

from .models import Genre, Book, NewsEmail
from users.models import CustomUser
from .sutility import get_client_ip


def home(request):

	if request.method == 'POST':
		ip = get_client_ip(request)

		news_email = NewsEmail()
		news_email.ip = ip
		news_email.email = request.POST['email']
		news_email.save()
		return redirect('home')
	else:
		data = dict()
		data['genres'] = Genre.objects
		data['suggests'] = Book.objects.filter(suggest=True)
		data['number_of_books'] = Book.objects.count()
		data['number_of_users'] = CustomUser.objects.count()
		return render(request, 'home.html', data)
