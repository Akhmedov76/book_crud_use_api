from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app_books.models import AuthorModel, BookModel
from app_books.serializers import AuthorSerializer, BookSerializer


@api_view(['GET', 'POST'])
def author_list_create(request):
    if request.method == 'GET':
        authors = AuthorModel.objects.all()
        serializer = AuthorSerializer(authors, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'status': True,
            'message': "Author created successfully",
            'data': serializer.data,
        }
        return Response(response, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'PATCH', 'DELETE'])
def author_detail(request, pk):
    author = get_object_or_404(AuthorModel, pk=pk)
    if request.method in ['PUT', 'PATCH']:  # Clean code uchun juda foydali ekan
        serializer = AuthorSerializer(author, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response = {
                'status': True,
                'message': "Author updated successfully",
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        author.delete()
        response = {
            'status': True,
            'message': "Author deleted successfully",
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def book_list_create(request):
    if request.method == 'GET':
        books = BookModel.objects.all()
        serializer = BookSerializer(books, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response = {
                'status': True,
                'message': "Book created successfully",
                'data': serializer.data,
            }
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH', 'DELETE'])
def book_detail(request, pk):
    book = get_object_or_404(BookModel, pk=pk)
    if request.method in ['PUT', 'PATCH']:
        serializer = BookSerializer(book, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response = {
                'status': True,
                'message': "Book updated successfully",
                'data': serializer.data,
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        book.delete()
        response = {
            'status': True,
            'message': "Book deleted successfully",
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
