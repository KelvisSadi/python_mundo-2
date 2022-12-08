print('Progressão aritimética com While')
primeiro_termo = int(input('Digite o primeiro termo da PA:'))
razao = int(input('Digite a razão da PA:'))
contador = 1
termo_final = 10
while contador <= termo_final:#enquanto {contador} for menor que {termo_final} faça
    print(contador, 'ª termo = ', primeiro_termo, end=' | ')#printa {contadorª} e primeiro termo
    primeiro_termo += razao#soma {primeiro_termo} com a {razão}
    if contador == termo_final:#se {contador} igual ao termo final faça: vai dar oportunidade de acrescentar mais termos
        termo_final += int(input('\nEstes foram os termos! Quer ver mais quantos?:'))
    contador += 1  # soma 1 em {contador}
print(f'A progressão foi finalizada com {contador - 1} termos mostrados')
#lógica contador começa com 1
#termo_final com 11
#while contador < termo_final vai rodar adicionando += 1 no contador, quando contador chegar a 10
#quando contador == termo_final, da a chance de atualizar o termo_final adicionando mais termos a serem vistos e assim continua se usuario apertar 0 acaba

