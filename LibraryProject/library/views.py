# library/views.py
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from .models import LibraryUser
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction
from django.utils import timezone


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = LibraryUser.objects.all()
    serializer_class = UserSerializer


class CheckOutBook(APIView):
    def post(self, request):
        book_id = request.data.get('book_id')
        user = request.user

        try:
            book = Book.objects.get(id=book_id)
            if book.copies_available > 0:
                Transaction.objects.create(user=user, book=book)
                book.copies_available -= 1
                book.save()
                return Response({"message": "Book checked out successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "No copies available"}, status=status.HTTP_400_BAD_REQUEST)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

class ReturnBook(APIView):
    def post(self, request):
        transaction_id = request.data.get('transaction_id')

        try:
            transaction = Transaction.objects.get(id=transaction_id, return_date__isnull=True)
            transaction.return_date = timezone.now()
            transaction.save()

            book = transaction.book
            book.copies_available += 1
            book.save()

            return Response({"message": "Book returned successfully"}, status=status.HTTP_200_OK)
        except Transaction.DoesNotExist:
            return Response({"error": "Transaction not found or already returned"}, status=status.HTTP_404_NOT_FOUND)

