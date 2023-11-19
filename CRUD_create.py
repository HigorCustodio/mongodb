
#* O QUE É UM CRUD (CREATE, READ, UPDATE, DELETE)?

# É um acronimo para as maneiras de se operar em informações armazenadas, são as quatro maneiras: create(criar), read(ler), update(atualizar), delete(deletar);

#CRUD tipicamente refere-se a operações perfomadas em um banco de dados ou base de dados, mas também pode aplicar-se para funções de alto nível de uma aplicação, como exclusões reversíveis, onde a informação não é realmente deletada, mas é marcada como deletada via status.

from pymongo import MongoClient
import json

#uri do banco 
#mongodb://user:password@host:port
uri = "mongodb://root:example@localhost:27017"
# uri = "mongodb://localhost:27017"

#agregando o banco para uma variavel client
client = MongoClient("localhost", 27017)

database = client['estudos_mongo']
collection = database['pessoas']

#* CRUD - CREATE

#*Inserindo um dado no banco de dados:
#? collection.insert_one(
#?        {
#?            "id":1,
#?            "nome":"Elismar"
#?        }
#?)

#* Inserindo varios dados no banco de dados
#Como são mais de um ele precisa ser uma lista de dados:

#? collection.insert_many(
#?     [
#?         {
#?             "id":2,
#?             "nome":"João"
#?         },   
#?         {
#?             "id":3,
#?             "nome":"José"
#?         }
#?     ]
#? )

#exemplos de funções insert:

#inserir 1 dado:
def inserir_1_dado(**args):
    collection.insert_one(args)

#inserir muitos dados:
def inserir_dados(dado):
    collection.insert_many(dados)

dados = [
    {"nome":"matias", "idade":25},
    {"nome":"fabio", "idade":28}
    ]
    

# inserir_dados(dado=dados)    
# inserir_1_dado(nome='eduardo', idade=15)

#print(list(collection.find()))
if __name__ == '__main__':
    inserir_1_dado(nome='eduardo', idade=15)
    inserir_dados(dado=dados)    




