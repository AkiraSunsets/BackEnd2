from rest_framework import serializers #serializers transforma o arquivo em json
from .models import Autor, Book, Publisher

class AutorSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Autor 
        fields = '__all__' #seleciona todos os campos do model Autor

class PublisherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'
        
class BookSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Book
        fields = '__all__' #seleciona todos os campos do model Book
