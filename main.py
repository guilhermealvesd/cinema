#Importa Biblioteca

import os

#Recebe o nome e idade do usuário

nome = input('Informe seu nome: ')
idade = str (input('Informe a sua idade: ')).replace(',','.')

#Convertendo a idade em float

idade = float(idade)

#Limpa Console

os.system('cls')

#Inicia o loop

while True:

    #Exibe a lista de filmes e suas salas

    print('LISTA DE FILMES\n')
    print('Sala 1 - A volta dos que não foram')
    print('Sala 2 - A Roda Quadrada')
    print('Sala 3 - Poeira em Alto Mar')
    print('Sala 4 - As Tranças do Rei Careca')
    print('Sala 5 - A Vingança do Peixe Frito')

    #Recebe a sala escolhida

    sala = int(input('Informe a sala desejada: '))

    #Classificação dos filmes

    match sala:
        case '1':
            idade_minima = 16
            break
        case 2:
            idade_minima = 16
            break
        case 3:
            idade_minima = 16
            break
        case 4:
            idade_minima = 16
            break
        case 5:
            idade_minima = 16
            break
        case _:
            print('Sala inexistente.')
            continue

    if idade >= idade_minima:
        print(f'Ingresso liberado para {nome}. Bom filme!')
        break
    else:
        print(f'Ingresso não permitido para {nome}')
        continue