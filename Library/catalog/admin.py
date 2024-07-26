from django.contrib import admin
from .models import Author,Book, BookInstance, Genre, Language

"""
This class is usually where classes are registered on djanjo sites.

#How the models were first registered

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookInstance)

In order to personalize django's admin site view of author, create a AuthorAdmin class. By default django's admin site
displays the the lists based on __str(), but the use of admin model classes allow to change that behaviour.

To create and edit new models the @register decorator will be used from now on

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

#Then register the model
admin.site.register(Author, AuthorAdmin)

Set list_display to control which fields are displayed on the change list page of the admin.

Example:

list_display = ["first_name", "last_name"]

"""

#Admin classes

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'birth_date', 'death_date')
    fields = ['first_name', 'last_name', ('birth_date', 'death_date')]

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    inlines = [BooksInstanceInline]
    display_genre.short_description = 'Genre'



@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
     list_filter = ('status', 'reservation_date')
     
     fieldsets = (
         (None,{
            'fields' : ('book','imprint', 'id')
         }),
         ('Availability',{
             'fields' : ('status', 'reservation_date')
         }),
     )

# Unregister the previous models
admin.site.unregister(Book)
admin.site.unregister(Author)
admin.site.unregister(BookInstance)


#Model registration
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Genre)
admin.site.register(Language)