from datetime import date #importa da biblioteca datetime a data(date)
print('lê 7 anos de nascimento e diz quantos deles atingiram a maioridade e quantos não')
maiores = 0
menores = 7
ano_atual = date.today().year
for analise in range(7):#laço analise no range de 7 vezes
    nasc = int(input(f'Em que ano a {analise + 1}ª pessoa nasceu?'))
    if (ano_atual - nasc) >= 18:#se idade for maior ou igual a 18. Lógica = menores começa com 7, a cada maior de 18 subtrai 1 de menores e soma 1 em maiores
        maiores += 1#vai somar 1 em maiores
        menores -= 1#vai subtrair 1 em menores
print(f'{menores} pessoas MENORES de idade! \n{maiores} pessoas MAIORES de idade!')
