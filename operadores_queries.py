
from pymongo import MongoClient

#agregando o banco para uma variavel client
client = MongoClient("localhost", 27017)


database = client['estudos_mongo']
collection = database['pessoas']

print(collection)

def busca_por_idade():
    collection.find_many(
        {'idade':{'$eq':15}}
    )

#! Operadores de queries - Comparação:
#* - $eq: Igual a(==);
#* - $ne: Diferente de(!=);
#* - $gt: Maior que(>);
#* - $qte: Maior ou igual(>=);
#* - $It: Menor que(<);
#* - $Ite: Menor ou igual(<=);
#* - $in / $nin: Igual(ou diferente) a um do array;

#*Exemplos:
print(busca_por_idade())
# busca_por_idade('$ne', 16)
# busca_por_idade('$gt', 27)
# busca_por_idade('$qte', 20)
# busca_por_idade('$It', 20)
# busca_por_idade('$Ite', 18)
# busca_por_idade('$In', 18)