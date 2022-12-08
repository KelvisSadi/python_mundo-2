print('Lê nome, idade sexo de 4 pessoas e mostra: Média de idade do grupo, qual é o nome do homem mais velho ')
homem_mais_velho = ''
mais_velho_idade = 0
qtd_mulher_menos_20 = 0
media = 0
nb = 0
#Lógica se sexo igual a 1,2 ou 3 sempre vamos somar idade em media, se feminino vamos ver se tem menos de 20 anos, se masculino vamos salvando o mais velho e substituindo caso necessário
for verfica in range(4):#laço verifica no range de 4 vezes
    nome = str(input('Digite o nome:'))
    idade = int(input(f'Digite a idade de {nome}:'))
    sexo = int(input('Digite [ 1 ] para feminino, [ 2 ] para masculino ou [ 3 ] para outro!'))
    media += idade
    if sexo == 1:#se sexo igual a 1 faça
        if idade < 20:#se sexo igual 1 e se idade menor que 20 faça
            qtd_mulher_menos_20 += 1#vai somar mais um em qtd..
    elif sexo == 2:#se sexo igual a 2
        if idade > mais_velho_idade:#se sexo igual a 2 e se idade maior que mais velho idade faça
            homem_mais_velho = nome#h_m_v vai receber nome
            mais_velho_idade = idade#mais velho idade vai receber idade
    elif sexo == 3:#se sexo igual a 3
       nb += 1
    else:
        print('Digite [ 1 ], [ 2 ] ou [ 3 ] para escolher o sexo!')
media = media / 4
print(f'A média de idade do grupo é {media:.1f} anos\nO homem mais velho é {homem_mais_velho} com {mais_velho_idade} anos\nAo todo tem {qtd_mulher_menos_20} mulheres com menos de 20 anos!')
if nb > 0:
    print(f'Ao todo tem {nb} pessoas não identificadas com homem ou mulher')