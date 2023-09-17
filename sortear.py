import  random
import os

erros = 0
sortear = random.randrange(0,20)
jogador = int(input('Digite um numero: '))

while(sortear != jogador):
    os.system(('cls'))
    if(sortear > jogador ):
        print('ERRO! O numero é maior')
    elif(sortear < jogador):
        print('ERRO! O numero é menor')
    erros+= 1
    jogador = int(input('Digite um numero: '))
print('Numero ' + str(jogador) + ', você acertou em ' + str(erros+1) + ' tentativas')
