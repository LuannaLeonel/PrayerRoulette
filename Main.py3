import cmd
import os

data_file = open('data.txt', "a")

with open('data.txt', 'r') as file:
    name_list = file.readlines()


def addlista():
    print("Adicione multiplos nomes à lista, depois de cada nome pressione enter e quando concluir digite '.' ")
    ans = True
    while ans:
        nome = input()
        if not (nome.endswith(".")):
            data_file.writelines(nome + '\n')
        else:
            ans = False


def menu():

    option = int(input('''O Que deseja fazer?
    1 - NOVO SORTEIO
    2 - ADICIONAR NOME
    3 - REMOVER NOME
    4 - EXIBIR LISTA DE NOMES
    5 - Sair
    '''))

    if option == 1:
        sortear()
        menu()
        pass
    elif option == 2:
        add_nome(str(input("Digite o nome a ser adicionado: ")))
        menu()
        pass
    elif option == 3:
        remove_nome(input("Digite o nome a ser removido: "))
        menu()
        pass
    elif option == 4:
        exibir()
        menu()
        pass
    elif option == 5:
        exit()
    else:
        print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE")
        menu()


def contains(nome):
    value = False
    for name in name_list:
        if name.strip("\n") == nome:
            value = True
    return value


def add_nome(nome):

    if not contains(nome):
        data_file.writelines(nome)
    else:
        print("nome já existe na lista")


def remove_nome(nome):

    if contains(nome):
        with open('data.txt', 'w') as f:
            for name in name_list:
                if name.strip("\n") != nome:
                    f.writelines(name)
    else:
        print("Nome não encontrado, insira um nome válido")


def sortear():
    "TODO fazer as combinacoes e pensar no que fazer quando a qnt de pessoas for impar"
    print("I'm working on it :)")
    return True


def exibir():
    temp = []
    for name in name_list:
        temp.append(name.strip("\n"))
    temp = sorted(temp)
    cli = cmd.Cmd()
    cli.columnize(temp, displaywidth=20)


if __name__ == '__main__':
    if os.stat('data.txt').st_size == 0:
        addlista()

    else:
        menu()
