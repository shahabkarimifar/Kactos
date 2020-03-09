from django.contrib import admin
from .models import Genre, Book, NewsEmail


class GenreAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'father_id')
	list_filter = ('name', 'father_id')

	fieldsets = ((None, {'fields': ('icon', 'name', 'father_id',)}),)
	add_feildsets = ((None, {'classes': ('wide',),
							 'fields': ('icon', 'name', 'father_id',)}),)

	ordering = ('id',)
	search_fields = ('name',)



class PdfAdmin(admin.ModelAdmin):

	list_display = ('title', 'genre', 'writer', 'uploader', 'stars', 'suggest', 'upload_date')
	list_filter = ('writer', 'genre', 'stars', 'upload_date', 'suggest')

	fieldsets = ((None, {'fields': ('cover', 'title', 'genre', 'writer', 'summary', 'stars', 'uploader', 'file', 'upload_date', 'suggest')}),)
	add_fieldsets = ((None, {'classes': ('wide',),
								'fields': ('cover', 'title', 'genre', 'writer', 'summary', 'stars', 'uploader', 'file', 'suggest', 'upload_date')}),)

	search_fields = ('title', 'genre', 'uploader', 'writer')
	ordering = ('title',)


class NewsEmailAdmin(admin.ModelAdmin):
	list_display = ('ip', 'email', 'joined_date')
	list_filter = ('joined_date', )

	fieldsets = ((None, {'fields': ('ip', 'email', 'joined_date')}),)
	add_fieldsets = ((None, {'classes': ('wide',),
							 'fiedls': ('ip', 'email', 'joined_date')}),)
	ordering = ('ip',)
	search_fields = ('ip', 'email',)



admin.site.register(Book, PdfAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(NewsEmail, NewsEmailAdmin)