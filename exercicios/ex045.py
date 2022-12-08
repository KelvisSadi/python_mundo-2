from random import randint
print('JoKenPO')
print('''Escolha
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
player = int(input('Sua escolha:'))
bot = randint(0, 2)
itens = ('Pedra', 'Papel', 'Tesoura')
#empate
if player == bot:
    resultado = ' Empate '
    #vitórias player
elif player == 0 and bot == 2 or player == 1 and bot == 0 or player == 2 and bot == 1:
    resultado = ' Player Vence '
#vitórias computador
else:
    resultado = ' Computador vence '
#game
if player < 3:
    print(f'''{resultado:=^58}
{f"Computador escolheu[{itens[bot]}]":^58}
        
{"--- vs ---":^58} 
        
{f"Player escolheu[{itens[player]}]":^58}
{" fim ":=^58}
        ''')
else:
    print('Opção invalida digite [ 0 ], [ 1 ] ou [ 3 ]')