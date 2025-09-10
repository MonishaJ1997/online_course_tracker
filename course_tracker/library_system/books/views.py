from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from django.shortcuts import render

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Serve frontend
def home(request):
    return render(request, "index.html")
