from math import sqrt

ca = float(input('Informe o valor (cm) do cateto adjacente: '))
co = float(input('Informe o valor (cm) do cateto oposto: '))

hipotenusa = sqrt(ca**2+co**2)

print(f'A hipotenusa é {hipotenusa}')

