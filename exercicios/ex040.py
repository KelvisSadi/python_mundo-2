print('Sistema de Avaliação')
nota_1 = float(input('Digite a nota da primeira prova:'))
nota_2 = float(input('Digite a nota da segunda prova:'))
media = (nota_1 + nota_2) / 2
if media >= 7.0:
    print(f'Sua média foi de {media:.2f} pontos. APROVADO!')
elif 5.0 <= media < 7.0:
    print(f'Sua média foi de {media:.2f} pontos. RECUPERAÇÃO!')
else:
    print(f'Sua média foi de {media:.2f} pontos. REPROVADO!')
