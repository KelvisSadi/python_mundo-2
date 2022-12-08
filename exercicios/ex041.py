from datetime import date
print('Confederação Nacional de Natação - Sistema de categorias')
nasc = int(input('Digite seu ano de nascimento:'))
idade = date.today().year - nasc
if idade <= 9:
    print(f'Com {idade} anos, você compete na categoria: MIRIM!')
elif idade <= 14:
    print(f'Com {idade} anos, você compete na categoria: INFANTIL!')
elif idade <= 19:
    print(f'Com {idade} anos, você compete na categoria: JUNIOR!')       #Não precisa verificar se tem mais de 14, porque se passou pelo de cima quer dizer que sim!
elif idade <= 25:
    print(f'Com {idade} anos, você compete na categoria: SÊNIOR!')
else:
    print(f'Com {idade} anos, você compete na categoria: MASTER!')