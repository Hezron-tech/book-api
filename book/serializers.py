from dataclasses import field
from rest_framework import serializers

from book.models import Book

class BookSerializer(serializers.Serializer):
    class Meta:
        Model = Book
        fields =('id','title','number_of_pages','publish_date','quantity')


        def create(self,data):
            return Book.objects.create (**data)