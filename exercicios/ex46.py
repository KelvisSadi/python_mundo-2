from time import sleep
print(f'\033[1;97;43m{" Vai começar os fogos de artifícios ":=^96}\033[m')
for tempo in range(10, 0, -1):#laço tempo no range de 10 a 0, diminuindo -1
    print(f'\033[1;31;107m{ tempo :-^96}\033[m')
    sleep(1)
for explosão in range(3):#laço explosão no range de 3 vezes
    sleep(0.5)
    print(f'\033[1;97;43m{"* * % | # ¨ $ / * *"* 5} \033[m')
    sleep(0.5)
    print(f'\033[1;35;48m{"* * % | # ¨ $ / * *" * 5} \033[m')
