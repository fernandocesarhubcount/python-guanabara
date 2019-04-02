altura = ""
comprimento = ""
area = 0
tinta = 0

while not altura.isdigit():
    altura = input('Digite a altura: ')

    if not altura.isdigit():
        print('O valor não é um valor válido')

while not comprimento.isdigit():
    comprimento = input('Digite a altura: ')

    if not comprimento.isdigit():
        print('O valor não é um valor válido')

area = float(altura) * float(comprimento)
tinta = area/2

print('Sua parede possui {} metros quadrados.'.format(area))
print('Você precisará de {} litros de tinta.'.format(area/2))
