import json

data = {}


def addlista():
print("Adicione multiplos nomes à lista, depois de cada nome pressione enter e quando concluir digite '.' ")
while True:
    nome = input()
    if not (nome.endswith(".")):
        data['Pessoa'].append({'nome': nome})

