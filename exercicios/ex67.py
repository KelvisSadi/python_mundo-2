print('Tabuada V3')
n = 0
while True:
    print('-'*40)
    n = int(input('Quer ver a tabuada de qual valor?'))
    print('-'*40)
    if n <= 0:
        print('Tabuada encerrada. Volte sempre!')
        break
    for t in range(1, 11):
        res = n * t
        print(f'{f"{n:<3} X {t:3} = {res:<3}":^40}')
