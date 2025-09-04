from django.shortcuts import render #render é de renderizar o template
from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import api_view, permission_classes #visualização do autor
from rest_framework.response import Response
from .models import Autor, Book, Publisher
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .serializers import AutorSerializers, BookSerializers, PublisherSerializers
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def visualizacao_autor(request):
    if request.method == 'GET':
        queryset = Autor.objects.all()
        serializer = AutorSerializers(queryset, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AutorSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
####################################################
class AutoresView(ListCreateAPIView):
    queryset = Autor.objects.all() #retorna todos os autores
    serializer_class = AutorSerializers #utiliza o serializer AutorSerializers para transformar o model em json
    permission_class = [IsAuthenticated] 
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['id']
    search_fields = ['name']  
    
     
class AutoresDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializers
    
###################################################

class BooksView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BooksDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = AutorSerializers

#######################################################

class PublisherView(ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = BookSerializers

class PublisherDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = AutorSerializers
    
#########################################################