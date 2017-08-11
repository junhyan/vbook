from rest_framework import serializers
from vbook.models import Book

class BookSerilizer(serializers.Serializer):

    book_id = serializers.CharField(required=True)  
    book_name = serializers.CharField(max_length=50)  
    book_author = serializers.CharField(max_length=50)  
    book_date = serializers.CharField(max_length=50)  
