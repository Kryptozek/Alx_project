from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, UserViewSet, CheckOutBook, ReturnBook

# Create a router for viewsets
router = DefaultRouter()
router.register('books', BookViewSet, basename='book')
router.register('users', UserViewSet, basename='user')

# Define additional paths for APIView-based endpoints
urlpatterns = [
    path('checkout/', CheckOutBook.as_view(), name='checkout'),
    path('return/', ReturnBook.as_view(), name='return'),
]

# Include router URLs
urlpatterns += router.urls
