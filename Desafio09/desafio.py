valor = ""
count = 0

while not valor.isnumeric():
    valor = input('Digite um valor inteiro: ')

    if not valor.isnumeric():
        print('O valor não é um número inteiro')

valor = int(valor)

while count <= 10:
    print("{} * {} = {}".format(valor, count, valor*count))
    count += 1
