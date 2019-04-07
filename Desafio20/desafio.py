import random

numeroOrdem = 0
listaNome = []

while len(listaNome)<4:
    listaNome.append(input(f'Digite o nome do aluno {len(listaNome)+1}: '))

print('A ordem será:\n')

random.shuffle(listaNome)
print(listaNome)

#tamanhoListaNome = len(listaNome)
#
#while tamanhoListaNome>0:
#    numeroOrdem = random.randint(0,tamanhoListaNome-1)
#    print(f'{5-tamanhoListaNome}: {listaNome[numeroOrdem]}')
#    listaNome.pop(numeroOrdem)
#    tamanhoListaNome = len(listaNome)
