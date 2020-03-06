from django.contrib import admin
from .models import Genre, Book


class GenreAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'father_id')
	list_filter = ('name', 'father_id')

	fieldsets = ((None, {'fields': ('name', 'father_id',)}),)
	add_feildsets = ((None, {'classes': ('wide',),
							 'fields': ('name', 'father_id',)}),)

	ordering = ('id',)
	search_fields = ('name',)



class PdfAdmin(admin.ModelAdmin):

	list_display = ('title', 'genre', 'uploader', 'stars', 'upload_date')
	list_filter = ('genre', 'stars', 'upload_date')

	fieldsets = ((None, {'fields': ('cover', 'title', 'genre', 'summary', 'stars', 'uploader', 'file', 'upload_date')}),)
	add_fieldsets = ((None, {'classes': ('wide',),
								'fields': ('cover', 'title', 'genre', 'summary', 'stars', 'uploader', 'file', 'upload_date')}),)

	search_fields = ('title', 'genre', 'uploader',)
	ordering = ('title',)



admin.site.register(Book, PdfAdmin)
admin.site.register(Genre, GenreAdmin)