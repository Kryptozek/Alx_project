from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, UserViewSet, CheckOutBook, ReturnBook

router = DefaultRouter()
router.register('books', BookViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('checkout/', CheckOutBook.as_view()),
    path('return/', ReturnBook.as_view()),
]
