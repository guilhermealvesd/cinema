#Recebe o nome e idade do usuário

nome = input('Informe seu nome: ')
idade = str (input('Informe a sua idade: ')).replace(',','.')

#Convertendo a idade em float

idade = float(idade)

#Exibe a lista de filmes e suas salas

print('LISTA DE FILMES\n')
print('Sala 1 - A volta dos que não foram')
print('Sala 2 - A Roda Quadrada')
print('Sala 3 - Poeira em Alto Mar')
print('Sala 4 - As Tranças do Rei Careca')
print('Sala 5 - A Vingança do Peixe Frito')

#Recebe a sala escolhida

while True:

    sala = int(input('Informe a sala desejada: '))

    #Classificação dos filmes


    match sala:
        case 1:
            if idade <12:
                print(f'{nome}, o filme escolhido está liberado - Classificação Livre.')
        case 2:
            if idade >=12:
                print(f'{nome}, o filme escolhido está liberado - Classificação 12 anos.')
        case 3:
            if idade >=14:
                print(f'{nome}, o filme escolhido está liberado - Classificação 14 anos.')
        case 4:
            if idade >=16:
                print(f'{nome}, o filme escolhido está liberado - Classificação 16 anos.')
        case 5:
            if idade >=18:
                print(f'{nome}, o filme escolhido está liberado - Classificação 18 anos.')
        case _:
            print('Filme escolhido não é permitido para esta idade')
            