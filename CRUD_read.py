
from pymongo import MongoClient

#agregando o banco para uma variavel client
client = MongoClient("localhost", 27017)


database = client['estudos_mongo']
collection = database['pessoas']


#! CRUD - READ

#*Buscar dados que contenham o(s) conjunto(s) de chave:valor especificado (retorna uma lista de dados)
#? Função: collection.find({key:value})


    #*Irá buscar os dados dentro do banco de dados através do conjunto chave e valor passado para a função collection.find({key:value})
    #exemplo:collection.find({'nome':'eduardo'})
    #resposta: <pymongo.cursor.Cursor object at 0x0000018F2B927B50>
    # print(collection.find({'nome':'eduardo'}))#!exemplo pratico

    #*Para acessar a lista de objetos de resposta basta utilizar o comando list() e inserir como argumento a função collection.find({'nome':'eduardo'}):
    #exemplo: list(collection.find({'nome':'eduardo'}))
    #resposta: [{'_id': ObjectId('63fbe1afac2bc105623554b7'), 'nome': 'eduardo', 'idade': 15}, {'_id': ObjectId('63fbe8892af1035d2b9336cc'), 'nome': 'eduardo', 'idade': 15}, {'_id': ObjectId('63fbe89079cdd9a06d5ee789'), 'nome': 'eduardo', 'idade': 15}, {'_id': ObjectId('63fbe89248495b55d74a78dd'), 'nome': 'eduardo', 'idade': 15}]
    # print(list(collection.find({'nome':'eduardo'})))#!exemplo pratico


#* Buscando um dado: Retorna o primeiro dado da collection ou se passado o conjunto chave:valor busca somente o primeiro dado encontrado que corresponda a esse conjunto chave e valor;
#? Função: collection.find_one()

    #*Para retornar o primeiro dado da collection sem filtros:
    # exemplo: collection.find_one()
    # resposta: {'_id': ObjectId('63fbe01a77814249625c2bf8'), 'id': 2, 'nome': 'Higor'}
    #print(collection.find_one())#!exemplo pratico
    
    #*Para retornar o primeiro dado da collection que se enquadre no conjunto chave:valor:
    # exemplo: collection.find_one({"key":"value"})
    # resposta: {'_id': ObjectId('63fbe1afac2bc105623554b7'), 'nome': 'eduardo', 'idade': 15}
    #print(collection.find_one({"nome":"eduardo"}))#!exemplo pratico
    
#exemplo de função:
def read_varios_registros(**args): #varios registros
    #ou find_many()
    collection.find(
        {}
        )
    
def read_um_registro(**args): #1 registros
    collection.find_one()

