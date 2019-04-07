import random

numeroUser = 1

while numeroUser != 0:

    numeroPC = random.randint(0,5)

    numeroUser = int(input('Digite um numero entre 0 e 5: '))

    if numeroPC == numeroUser:
        print(f'Você venceu! PC: {numeroPC} e Você: {numeroUser}')
    else:
        print(f'Você perdeu! O PC escolheu o número {numeroPC}')
