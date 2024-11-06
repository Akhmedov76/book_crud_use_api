from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app_books.models import AuthorModel


@api_view(['GET', 'POST'])
def author_list_create(request):
    if request.method == 'GET':
        authors = AuthorModel.objects.all()
        serializer = AuthorSerializer(authors, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response = {
                'status': True,
                'message': "Author created successfully",
                'data': serializer.data,
            }
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
