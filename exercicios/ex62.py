print('Progressão Aritmética - Jeito Guanabara')
primeiro_termo = int(input('Digite o primeiro termo da PA:'))
razao = int(input('Digite a razão da PA:'))
contador = 1
termo_final = 10
mais = 1
while mais != 0:#enquanto mais diferente de 0, ele vai rodar o bloco
    while contador <= termo_final:#enquanto contador menor ou igual termo_final ele vai rodar o bloco
        print(contador, 'ª termo = ', primeiro_termo, '|', end=' ')
        primeiro_termo += razao
        contador += 1
    mais = int(input(f'\nEstes foram os termos da PA. Quer ver mais quantos?'))
    termo_final += mais#vai somar mais em termo_final, como era 10, se for mais 1, vai mostrar o 11ª termo, e etc...
print(f'Estes foram os {contador - 1} termos mostrados!')
