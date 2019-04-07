valorMaior = 0
numeros = 0

while numeros<3:
    valor = int(input('Digite um número: '))

    if numeros == 0:
        valorMaior = valor
    else:
        if valorMaior<valor:
            valorMaior = valor
    numeros+=1

print(f'O maior valor entre eles é o {valorMaior}')
