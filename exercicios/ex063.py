print('Sequência de Fibonacci')
n = int(input('Digite um número:'))
antes = 1
atual = 0
proximo = 0
while n > 0:
    proximo = antes + atual#Lógica: Primeiro calculamos o proximo termo com a soma dos dois termos de trás
    print(proximo)#depois mostramos o termo que foi calculado
    antes = atual#o termo mais antigo recebe o do meio
    atual = proximo#e o termo do meio recebe o que foi calculado, assim todos os termos foram atualizados e podemos calcular o próximo no looping
    n -= 1
print('teste')
print('olá')