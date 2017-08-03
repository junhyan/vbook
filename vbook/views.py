from django.http import HttpResponse
from django.http import Http404
from models import Book
from serializers import BookSerilizer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
import time


class GetAllBooks(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerilizer(books, many=True)
        return Response(serializer.data)


class BookManagement(APIView):
    def post(self, request, format=None):
        serializer = BookSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUSET)

    def get_book(self, book_id):
        try:
            return Book.objects.get(book_id = book_id)
        except Book.DoesNotExist:
            return Http404
    def get(self, request, book_id, format=None):
        book = self.get_book(book_id)
        serializer = BookSerilizer(book)
        return Response(serializer.data)
        
    def put(self, request, book_id, format=None):
        serializer = BookSerilizer(self.get_book(book_id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUSET)
        
    def delete(self, request, book_id, format=None):
        book = self.get_book(book_id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
