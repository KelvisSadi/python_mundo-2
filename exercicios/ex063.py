print('Sequência de Fibonacci')
n = int(input('Quantos termos quer mostrar:'))
antes = 1
atual = 0
proximo = 0
while n > 0:
    print(proximo, end=' -> ')  #depois mostramos o termo que foi calculado
    proximo = antes + atual#Lógica: Calculamos o {proximo} termo com a soma dos dois termos de anteriores
    antes = atual#o termo mais antigo recebe o do meio
    atual = proximo#e o termo do meio recebe o que foi calculado, assim todos os termos foram atualizados e podemos calcular o próximo no looping
    n -= 1
print('FIM')
#ex: [f1= 1, f2= 0, f3=?] -> [f1= 1, f2= 0, f3= f1 + f2]