distancia = int(input('Digite a distância em km da viagem: '))

if distancia<=200:
    valor = distancia * 0.5
else:
    valor = distancia * 0.45

print(f'O valor da viagem é de R$ {valor:.2f}')
