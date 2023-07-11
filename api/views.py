from django.shortcuts import render
from rest_framework import viewsets
#from .serializers import ItemSerializer
#from .models import Item

from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

# Create your views here.
#class ItemViewSet(viewsets.ModelViewSet):
 #   queryset = Item.objects.all()
  #  serializer_class = ItemSerializer


class ListPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


