km = ''
dias = ''
pagamento = 0

while not km.isdigit():
    km = input('Digite a kilometragem: ')

    if not km.isdigit():
        print('O valor não é um valor válido')

while not dias.isnumeric():
    dias = input('Digite a quantidade de dias: ')

    if not dias.isnumeric():
        print('O valor não é um valor válido')

km = float(km)
dias = int(dias)

pagamento = float(60*dias)+0.15*km

print('Você deve pagar {:.2f} reais = R$ 60.00 x {:.2f} dias + R$ 0.15 x {:.2f} kilometros '.format(pagamento, dias, km))
