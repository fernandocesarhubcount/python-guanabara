import math

valor = int(input('Digite um número entre 0 e 9999: ')[0:4])

print(f'O número {valor} possui:')

print(f'unidade: {valor//1%10}')
print(f'dezena: {valor//10%10}')
print(f'centena: {valor//100%10}')
print(f'milhar: {valor//1000%10}')