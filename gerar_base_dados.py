from pymongo import MongoClient

#client = MongoClient("base de dados", "porta")
client = MongoClient("localhost", 27017)

#cria base de dados
db = client.Estudo_MongoDB

#Inserindo valores
#insert.many inserir diversos dados
db.test.insert_many(
    [
        {"id":1},
        {"id":12},
        {"id":500},
        {"id":-220}
    ]
)

