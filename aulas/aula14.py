r = 's'
while r == 's':
    n = int(input('Digite um valor:'))
    r = str(input('Quer continuar [S/N]')).lower()
print('FIM')
filmes = ['thor 3', 'Se ela dança, eu danço 2', 'Ta dando onda']
for filme in filmes:
    print(filme)
#estou aprendendo git
nome2 = str(input('Digita seu nome aí:'))
#exemplo: while para ler o nome de todos que chegarem no balcão hoje porque enquanto não chegar o horario final ele vai repetindo

#exemplo: for para ler o nome das primeiras 50 pessoas que se inscreverem no site
n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um número:'))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares')
#for com lista
lista = ['Joao', 'Maria', 'Jessica', 'Romario']
for nome in lista[::-1]:
    print(nome)