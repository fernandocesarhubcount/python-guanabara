valor = ""

while not valor.isdigit():
    valor = input('Digite o preço do produto: ')

    if not valor.isdigit():
        print('O valor não é um valor válido')

valor = float(valor)

print('O produto com preço de {:.2f} reais, fica {:.2f} reais com 5% de desconto'.format(valor, valor*0.95))
