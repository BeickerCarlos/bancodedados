import csv
from re import I
import pymongo

arquivo = "cadastro_estabelecimentos_cnes.csv"
url = "mongodb+srv://x:eduardo12344@cluster0.smtnsyk.mongodb.net/?retryWrites=true&w=majority"
myclient = pymongo.MongoClient(url)
mydb = myclient["meubanco"]
mycol = mydb["Lista-Alunos"]
with open(arquivo) as arquivoCSV:
    dados = csv.reader(arquivoCSV, delimiter=";", quotechar='"')
    next(dados)
    for linha in dados:
        c = linha[0]
        u = linha[1]
        i = linha[2]
        n = linha[3]
        lo = linha[4]
        b = linha[5]
        lat = linha[6]
        long = linha[7]
        dados = {f"'CNES':'{c}','UF':'{u}','IBGE':'{i}','Nome':'{n}','Logradouro':'{lo}','Bairro':'{b}','Latitude':'{lat}','Longitude':'{long}'"}
        print(dados)
        break