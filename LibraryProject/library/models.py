# library/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    copies_available = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class LibraryUser(AbstractUser):
    date_of_membership = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    groups = models.ManyToManyField(
        Group,
        related_name='libraryuser_set',  # Provide a unique related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='libraryuser_permissions_set',  # Provide a unique related_name
        blank=True
    )

class Transaction(models.Model):
    user = models.ForeignKey('LibraryUser', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    check_out_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
