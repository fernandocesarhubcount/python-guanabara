valor = ""

while not valor.isdigit():
    valor = input('Digite um valor em real: ')

    if not valor.isdigit():
        print('O valor não é um valor válido')

valor = float(valor)

print('{:.2f} reais = {:.2f} dólares'.format(valor, valor*3.27))
