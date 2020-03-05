from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	fom = CustomUserChangeForm
	model = CustomUser

	list_display = ('username', 'email', 'is_superuser', 'is_staff', 'is_active',)
	list_filter = ('email', 'is_staff', 'is_active',)

	fieldsets = (
		(None, {'fields': ('username', 'email', 'profpic', 'password')}),
		('Permissions', {'fields': ('is_staff', 'is_active')}),
		)

	add_fieldsets = (
		(None, {
			'classes': ('wdie',),
			'fields': ('username', 'profpic', 'email', 'password1', 'password2', 'is_superuser', 'is_staff', 'is_active')}
		),		
		)

	search_feilds = ('email', 'username')
	ordering = ('username',)


admin.site.register(CustomUser, CustomUserAdmin)