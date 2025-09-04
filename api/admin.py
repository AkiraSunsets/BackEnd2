from django.contrib import admin

from .models import * #asterisco importa todos os modelos

admin.site.register(Autor) 
#Registra o modelo Autor no site de administração do Django

admin.site.register(Book)

admin.site.register(Publisher)
#Registra o modelo Book no site de administração do Django

#PRA ADICIONAR NOVOS CAMPOS, ADICIONA AQUI KETY!!!!!!!!