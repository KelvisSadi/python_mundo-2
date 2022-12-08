print('Analisa a frase e diz se é um palindromo')
frase = str(input('Digite a frase que deseja analisar:')).upper().replace(' ', '')#joga pra minuscula e troca os espaços por sem espaços
invertida = frase[::-1]#variavel invertida recebe a frase invertida
print(f'O inverso de {frase} é {invertida}')
if frase == invertida:#se frase igual invertida faça. Lógica = um palindromo é a frase que é igual de tras para frente então invertemos a frase digitada e verificamos se é igual a frase normal
    print('É um palindromo!')
else:
    print('Não é um palindromo!')
