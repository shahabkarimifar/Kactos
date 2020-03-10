from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager
# from pdf.models import Book

class CustomUser(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(_('email address'), unique=True)
	username = models.CharField(max_length=300, unique=True)
	profpic = models.ImageField(upload_to='profpic/', null=True, blank=True) # profile picture
	bookshelf = models.ManyToManyField('pdf.Book')
	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	date_joined = models.DateTimeField(default=timezone.now)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username',]

	objects = CustomUserManager()

	def __str__(self):
		return self.username