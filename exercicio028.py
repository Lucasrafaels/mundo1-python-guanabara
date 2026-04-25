from random import randint
computador = randint(0,5)
print('='*100)
print ('Computador: Vamos jogar um jogo, se você acertar o número que estou pensando você ganha!')
print('='*100)
escolha = int(input ('Digite um número de 0 a 5: '))
if escolha == computador:
    print ('Parabéns, você ganhou o jogo eu estava pensando nesse mesmo número')  
else:
    print ('Você perdeu, eu estava pensando em {}' .format(computador))
