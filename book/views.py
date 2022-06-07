from django.shortcuts import render
from . models import Book
from rest_framework.response import Response
from rest_framework.decorators import api_view
from  book.serializers import  BookSerializer


# Create your views here.


@api_view(['GET'])
def book_list(request): 
    books = Book.objects.all()
    serializer= BookSerializer(books, many=True)
    return Response(serializer.data)
    
    
