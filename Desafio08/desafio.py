valor = ""
cent  = 0
mili  = 0

while not valor.isdigit():
    valor = input('Digite um valor em metro: ')

    if not valor.isdigit():
        print('O valor não é um número')

valor = float(valor)
cent  = valor*100
mili  = valor*1000

print("{} metros = {} centímetros = {} milímetros".format(valor, cent, mili))