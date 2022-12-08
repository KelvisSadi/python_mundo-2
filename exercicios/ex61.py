print('Progressão aritimética com While')
primeiro_termo = int(input('Digite o primeiro termo da PA:'))
razao = int(input('Digite a razão da PA:'))
termo = 1
termo_final = 11
while termo < termo_final:#enquanto {termo} for menor que {termo_final} faça
    print(termo, 'ª termo = ', primeiro_termo, end=' | ')#printa {termoª} e primeiro termo
    primeiro_termo += razao#soma {primeiro_termo} com a {razão}
    termo += 1#soma 1 em {termo}
    if termo == termo_final:#se {termo} igual ao termo final faça: vai dar oportunidade de acrescentar mais termos
        termo_final += int(input('\nEstes foram os termos! Quer ver mais quantos?:'))
#lógica termo começa com 1
#termo final com 11
#while termo < termo_final vai rodar adicionando += 1 no termo, quando termo chegar a 10
#quando termo == termo_final, da a chance de atualizar o termo final adicionando mais termos a serem vistos e assim continua se usuario apertar 0 acaba

