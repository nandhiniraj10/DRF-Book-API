# blog/urls.py
# urls.py
from django.urls import path
# from .views import BookAPIView
from .views import book_list, create_book

urlpatterns = [
    # path('books/', BookAPIView.as_view(), name='book-api'),
    path('books/', book_list, name='book-list'),
    path('books/create/', create_book, name='create-book'),
]

