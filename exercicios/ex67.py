print('Tabuada V3')
while True:  # while infinito n1
    print('-'*40)
    n = int(input('Quer ver a tabuada de qual valor?'))
    print('-'*40)
    if n <= 0:
        print('Tabuada encerrada. Volte sempre!')
        break  # break n1
    for tabuada in range(1, 11):
        res = n * tabuada
        print(f'{f"{n:<3} X {tabuada:3} = {res:<3}":^40}')
