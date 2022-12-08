nome = str(input('Qual é seu nome?'))
verificar = nome.strip().lower()
if 'kelvis' in verificar:
    print('Que nome lindo!')
elif 'marli' in verificar:
    print('Olá mãe!')
elif 'talisson' in verificar:
    print('Olá zeca!')
elif 'gelson' in verificar:
    print('Olá pai')
else:
    print('Individuo não reconhecido!')
print(f'Tenha um bom dia, {nome}!!!')