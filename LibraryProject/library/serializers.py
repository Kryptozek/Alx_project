
from rest_framework import serializers
from .models import Book, LibraryUser, Transaction

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryUser
        fields = ['id', 'username', 'email', 'date_of_membership', 'is_active']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
