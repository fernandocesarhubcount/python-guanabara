salario = ""

while not salario.isdigit():
    salario = input('Digite o salário: ')

    if not salario.isdigit():
        print('O valor não é um valor válido')

salario = float(salario)

print('O salário de {:.2f} reais, com o reajuste (15%), fica em {:.2f} reais'.format(salario, salario*1.15))
