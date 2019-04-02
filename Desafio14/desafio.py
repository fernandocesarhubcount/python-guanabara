temperatura = ""

while not temperatura.isdigit():
    temperatura = input('Digite a temperatura em celsius: ')

    if not temperatura.isdigit():
        print('O valor não é um valor válido')

temperatura = float(temperatura)

print('{:.2f} celsius = {:.2f} fahrenheit'.format(temperatura, temperatura*9/5+32))
