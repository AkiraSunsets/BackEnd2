import pandas as pd #importando a biblioteca pandas
from django.core.management.base import BaseCommand #importando a classe BaseCommand do Django
from django.db import transaction #importando afunção transaction do Django
from api.models import Autor #importando o modelo autor do arquivo models.py


class Command(BaseCommand): # define a classe command que herda de BaseCommand
    def add_arguments(self, parser): #define o método add_arguments que recebe um parser como argumento
        parser.add_argument("--arquivo", default="population/autores.csv") 
        parser.add_argument("--truncate", action="store_true")
        parser.add_argument("--update", action="store_true")
    
    @transaction.atomic #decorador que garante que todas as operações dentro do método sejam atômicas
    def handle(self, *a, **o): 
        df = pd.read_csv(o["arquivo"], encoding="utf-8-sig") #lendo o arquivo csv e armazenando em um dataframe
        df.columns = [c.strip().lower().lstrip("\ufeff") for c in df.columns] #removendo espaços em branco e convertendo para minúsculas os nomes das colunas

        if o["truncate"]: Autor.objects.all().delete() #se o argumento truncate for passado, deleta todos os registros da tabela autor
        
        df ["name"] = df["name"].astype(str).str.strip() #remove os espaços em branco dos nomes dos autores
        df ["last_name"] = df["last_name"].astype(str).str.strip() #remove os espaços em branco dos sobrenomes dos autores
        df ["birth_date"] = pd.to_datetime(df["birth_date"], errors = "coerce", format="%Y-%m-%d").dt.date #converte a coluna birth_date para o formato de data
        df ["nacionality"] = df.get("nacionality", "").astype(str).str.strip().str.capitalize().replace({"": None}) #remove os espaços em branco e capitaliza a nacionalidade dos autores
        
        df = df.query("name !='' and last_name != '' ") #filtra o dataframe para remover linhas com nome ou sobrenome vazio
        df = df.dropna(subset=["birth_date"]) #remove linhas com data de nascimento nula
        
        if o["update"]:
            criados = atualizados = 0
            for r in df.itertuples(index=False):
                _, created = Autor.objects.update_or_create(
                    nome = r.name, last_name = r.last_name, birth_date = r.birth_date, 
                    defaults= {"nacionality": r.nacionality}
                 ) #cria ou atualiza o registro do autor
                
                criados += int(created) #incrementa o contador de criados se o registro foi criado
                atualizados += int (not created) #incrementa o contador de atualizados se o registro foi atualizado
                self.stdout.write(self.style.SUCCESS(f"Criados: {criados} | Atualizados: {atualizados}")) #exibe uma mensagem de sucesso com o número de registros criados e atualizados
        else:
            objs = [Autor(
                name = r.name, last_name = r.last_name, birth_date = r.birth_date, nacionality = r.nacionality)
                    for r in df.itertuples(index=False)]
            Autor.objects.bulk_create(objs, ignore_conflicts=True) #cria os registros em massa, ignorando conflitos
            self.stdout.write(self.style.SUCCESS(f"Criados: {len(objs)}")) #exibe uma mensagem de sucesso com o número de registros criados