# # views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Book

@api_view(['GET'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        book_list = []
        for book in books:
            book_dict = {
                'id': book.id,
                'title': book.title,
                'author': book.author,
            }
            book_list.append(book_dict)
        return Response(book_list)

@api_view(['POST'])
def create_book(request):
    if request.method == 'POST':
        data = request.data
        title = data.get('title', '')
        author = data.get('author', '')

        if title and author:
            new_book = Book.objects.create(title=title, author=author)
            book_dict = {
                'id': new_book.id,
                'title': new_book.title,
                'author': new_book.author,
            }
            return Response(book_dict, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Title and author are required fields.'}, status=status.HTTP_400_BAD_REQUEST)

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Book

# class BookAPIView(APIView):
#     """
#     API View for handling books.
#     """
#     def get(self, request, format=None):
#         """
#         List all books.
#         """
#         books = Book.objects.all()
#         book_list = []
#         for book in books:
#             book_dict = {
#                 'id': book.id,
#                 'title': book.title,
#                 'author': book.author,
#             }
#             book_list.append(book_dict)
#         return Response(book_list)

#     def post(self, request, format=None):
#         """
#         Create a new book.
#         """
#         data = request.data
#         print(data)
#         title = data.get('title', '')
#         print(title)
#         author = data.get('author', '')

#         if title and author:
#             new_book = Book.objects.create(title=title, author=author)
#             book_dict = {
#                 'id': new_book.id,
#                 'title': new_book.title,
#                 'author': new_book.author,
#             }
#             return Response(book_dict, status=status.HTTP_201_CREATED)
#         else:
#             return Response({'error': 'Title and author are required fields.'}, status=status.HTTP_400_BAD_REQUEST)
            