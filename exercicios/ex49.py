print(f'{" Tabuada ":=^41}')
num = int(input('Digite um número para ver a tabuado dele:'))
for tabuada in range(1, 11):#laço tabuada no range de 1 a 11, ou seja, vai repetir o bloco dele 10 vezes
    print(f'{f" {num:}  x {tabuada:2} = {num * tabuada:2} ":=^41}')