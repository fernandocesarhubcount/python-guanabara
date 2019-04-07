velocidade = int(input('Digite a velocidade do carro (km/h): '))

if velocidade>80:
    print(f'Você foi multado! A multa é de R$ {(velocidade-80)*7:.2f}')

