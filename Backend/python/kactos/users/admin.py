from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	fom = CustomUserChangeForm
	model = CustomUser

	list_display = ('username', 'email', 'is_superuser', 'is_staff', 'is_active', 'is_admin')
	list_filter = ('email', 'is_staff', 'is_active', 'is_superuser', 'is_admin')

	fieldsets = (
		(None, {'fields': ('username', 'email', 'profpic', 'password')}),
		('Permissions', {'fields': ('is_staff', 'is_active', 'is_admin', 'is_superuser')}),
		)

	add_fieldsets = (
		(None, {
			'classes': ('wdie',),
			'fields': ('username', 'profpic', 'email', 'password1', 'password2', 'is_superuser', 'is_staff', 'is_active', 'is_admin')}
		),		
		)

	search_feilds = ('email', 'username')
	ordering = ('username',)


admin.site.register(CustomUser, CustomUserAdmin)