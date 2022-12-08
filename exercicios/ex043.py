print('Academia Kelvis - Calculo IMC')
peso = float(input('Digite seu peso [kg]:'))
altura = float(input('Digite sua altura[m]:'))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Seu calculo de IMC deu {imc:.1f}, você está abaixo do peso ideal!')
elif imc < 25:
    print(f'Seu calculo de IMC deu {imc:.1f}, você está no peso ideal!')
elif imc < 30:
    print(f'Seu calculo de IMC deu {imc:.1f}, você etá com sobrepeso!')
elif imc < 40:
    print(f'Seu calculo de IMC deu {imc:.1f}, você está com obesidade!')
else:
    print(f'Seu calculo de IMC deu {imc:.1f}, você está com obesidade mórbida!')
print('''
Tabela - IMC
MENOR QUE 18.5    - MAGREZA
ENTRE 18.5 E 24.9 - NORMAL
ENTRE 25 E 29.9   - SOBREPESO
ENTRE 30 E 39.9   - OBESIDADE
ACIMA DE 40       - OBESIDADE MÓRBIDA
''')