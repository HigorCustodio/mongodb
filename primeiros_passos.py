from pymongo import MongoClient
import json


#uri do banco 
#mongodb://user:password@host:port
# uri = "mongodb://root:example@localhost:27017"

#agregando o banco para uma variavel client
client = MongoClient("localhost", 27017)


#mostra os bancos de dados dentro do mongo localhost:27017
#?print(client)

#mostra as collections dentro do banco de dados
#?print(client.list_database_names())

#mostra o banco de dados "Estudos_Edu_Mongo_DB" e a collection "live_python" dentro do banco
#?print(client.Estudos_Edu_Mongo_DB.live_python)

#Mostra os objetos dentro da collection "live_python"
#?print(client.Estudos_Edu_Mongo_DB.live_python.find())

#Lista os objetos dentro da collection "live_python"
#?print(list(client.Estudos_Edu_Mongo_DB.live_python.find()))

#*Maneiras de atribuir variaveis com o banco de dados e collection:
#Tradicional:
# É o modelo tradicional devido ao fato de que com o uso de strings caso seja criado uma collection com espaço no nome(não é correto, mas é possivel) seja possivel acessa-la

#Criando variavel que representa o banco de dados 'Estudos_Mongo'
database = client['estudos_mongo']

#Criando variavel que representa a coleção 'pessoas' dentro do bd
collection = database['pessoas']
    # print(collection)#!temp
    
#Não tradicional:
#Caso seja criado uma collection com o nome contendo espaços não sera possivel acessa-la
#?database = client.estudos_mongo
#?collection = database.live_python

# Acessa o primeiro dado dentro da collection
collection.find_one()

# print(collection.find_one())
primeiro_dado = collection.find_one()

print(primeiro_dado['nome'])






