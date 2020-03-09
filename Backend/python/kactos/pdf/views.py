from django.shortcuts import render, redirect
from django.http import HttpRequest

from .models import Genre, Book, NewsEmail
from users.models import CustomUser


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


def get_client_ip(user_info):
	"""
		takes request variable as argument and returns client ip
	"""
	x_forwarded_for = user_info.META.get('HTTP_X_RORWARDED_FOR')

	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = user_info.META.get('REMOTE_ADDR')

	return ip
