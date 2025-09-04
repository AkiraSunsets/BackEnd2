from django.db import models

class Autor(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255) #NULL significa que o campo pode ser nulo
    birth_date = models.DateField(null=True, blank=True) #DateField campo de data
    nacionality = models.CharField(max_length=30, null=True, blank=True) # CharField campo de caracteres limitado
    biografy = models.TextField(null=True, blank =True) #TextField não tem limite de caracteres

    def __str__(self):
        return f"{self.name} {self.last_name}" #Representação em string do modelo Autor

class Publisher(models.Model):
    editora = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    site = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.editora
    
class Book(models.Model): #cria o campinho do Book bem de cria 
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=50)
    description = models.TextField()
    language = models.CharField(default='Portugues')
    year = models.IntegerField()
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    desconto = models.DecimalField(max_digits=10, decimal_places=2)
    disponibility = models.BooleanField(default=True)
    dimensions = models.CharField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.title} {self.autor}" #Representação em string do modelo Book