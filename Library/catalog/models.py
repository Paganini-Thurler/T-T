from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
import uuid
   
class Author(models.Model):
    """A model that represents the author"""
    
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField('Deceassed', null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def __str__(self):
        """ A method that will return a model's string representation"""
        return f'{self.last_name}, {self.first_name}'
    
    def get_absolute_url(self):
        """Returns a url to access an Author instance."""
        return reverse("author-detail", args=[str(self.id)])
    
    class Meta:
        """Defines how the table will be ordered"""
        ordering = ['last_name', 'first_name']

class Book(models.Model):
    """A model that represents a book"""
    
    #A book can have an author or not, consider that are anonimous authors
    author = models.ForeignKey(Author, on_delete=models.RESTRICT, null=True)
    #A book can have no definned genre or many at the same time.
    genre = models.ManyToManyField('Genre',help_text='Genre')
    #ISBN is a unique identifier that has 13 characters
    isbn = models.CharField(help_text='ISBN',max_length=13, name='ISBN',unique=True,null=True)
    summary = models.TextField(max_length=1000)
    title = models.CharField(max_length=200)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        """ A method that will return a string model's representation"""
        return self.title
    
    def get_absolute_url(self):
        """Returns a url to access a Book instance."""
        return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Book's unique identifier")
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    reservation_date = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('a', 'Available'),
        ('m', 'Maintencenance'),
        ('o','On loan'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1,choices=LOAN_STATUS, blank=True, default='a', help_text='Book availability')

    def __str__(self):
        """ A method that will return a string model's representation"""
        return f'{self.id} ({self.book.title})'
    
    class Meta:
        """Defines how the table will be ordered"""
        ordering = ['reservation_date']
    
    
class Genre(models.Model):
    """A model that represents a book's genre"""
    
    name = models.CharField(max_length=200,unique=True,help_text="Book's genre")
    
    def __str__(self):
        """A method that returnx a model's string representation"""
        return self.name
    
    def get_absolute_url(self):
        """Returns a url to access a genre instance."""
        return reverse("model_detail", args=[str(self.id)])
    
    class Meta:
        """Defines how the table will be ordered"""
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='genre_name_case_insentive_unique',
                violation_error_message = "Genre already exists in the database"
            ),
        ]

class Language(models.Model):
    """A model that represents a book's language"""
    
    name = models.CharField(max_length=40, unique=True, help_text='Natural language')
    
    def __str__(self):
        """A method that returns a model's string representation"""
        return self.name
    
    def get_absolute_url(self):
        """Returns a url to access the language"""
        return reverse('book-language', args=[str(self.id)])
    
    class Meta:
        constraints = [
            UniqueConstraint(Lower('name'),name='language_case_insensitive_unique', violation_error_message='Language already exists'),
        ] 