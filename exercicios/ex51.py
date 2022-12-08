print('Progressão aritmética - 10 termos')
primeiro_termo = int(input('Digite o primeiro termo:'))
razao = float(input('Digite a razão:'))
for prog in range(10):#laço prog no range de 10 vezes
    print(f'a{prog + 1} = {primeiro_termo:.0f}')
    primeiro_termo += razao#primeiro termo soma ele mais a razão
#lógica primeiro termo é mostrado, depois é somado ele com a razão e é mostrado o segundo termo ...
#jeito guanabara
primeiro = int(input('Digite o pimeiro termo:'))
razao2 = int(input('Digite a razão:'))
decimo = primeiro + (10 - 1) * razao2
for c in range(primeiro, decimo + razao2, razao2):
    print(c, end='->')