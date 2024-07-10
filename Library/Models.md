# Database UML


![UML](./documents/images/local_library_model_uml.svg)


The diagram also shows the relationships between the models, including their multiplicities. The multiplicities are the numbers on the diagram showing the numbers (maximum and minimum) of each model that may be present in the relationship. For example, the connecting line between the boxes shows that Book and a Genre are related. The numbers close to the Genre model show that a book must have one or more Genres (as many as you like), while the numbers on the other end of the line next to the Book model show that a Genre can have zero or many associated books.

# Defining a model 

```
from django.db import models
from django.urls import reverse

class MyModelName(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    # …

    # Metadata
    class Meta:
        ordering = ['-my_field_name']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.my_field_name
```
## Common field types 

- AutoField: A special type of IntegerField that automatically increments. A primary key of this type is automatically added to the model if one isn't specified .
- CharField: Use for short and medium size strings, max_length argument required.
- DateField: Use for dates
- DateTimeField: Use for time stamps
- EmailField: Use for email strings, it validates emails
- FileField: Use to store files.
- ForeignKey: Use to specify a one-to-many relationship.
- ImageField: Use to store images
- IntegerField: Use for integers.
- ManyToManyField: Use to specify a many-to-many relationship.
- TextField: Use for long strings or texts.

## Common field types arguments


# How to itereate on the collection

all_books = Book.objects.all()


Filter results
wild_books = Book.objects.filter(title__contains='wild')
number_wild_books = wild_books.count()

THe pattern is field + __ + contains/icontain/iexact/exact/in/gt/startswith

