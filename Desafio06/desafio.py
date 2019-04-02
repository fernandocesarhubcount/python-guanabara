valor = input('Digite um valor: ')

if not valor.isdigit():
    print('O valor não é um número!')
else:

    if valor.isnumeric():
        valor = int(valor)
    elif valor.isdecimal():
        valor = float(valor)
    else:
        valor = 0

    print('Valor: {}. Dobro = {}, Triplo = {} e Raiz Quadrada = {}'.format(valor, valor*2, valor*3, valor**2))
