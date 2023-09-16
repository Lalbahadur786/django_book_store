from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ('slug',)
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'rating')
    list_display = ('title', 'author', 'is_best_selling')


# Register your models here.
admin.site.register(Book, BookAdmin)

