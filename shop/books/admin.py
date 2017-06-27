from django.contrib import admin
from books.models import Publisher, Author, Book

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name',)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('publication_date', 'title', 'publisher')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    fields = ('title', 'publication_date', 'publisher', 'authors')
    raw_id_fields = ('publisher',)

admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
