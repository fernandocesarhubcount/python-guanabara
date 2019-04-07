import random

nome1 = input('Digite o nome do primeiro aluno: ')
nome2 = input('Digite o nome do segundo aluno: ')
nome3 = input('Digite o nome do terceiro aluno: ')
nome4 = input('Digite o nome do quarto aluno: ')

alunoSorteado = random.randint(1,4)
alunoSorteadoNome = ''

if alunoSorteado==1:
    alunoSorteadoNome = nome1

if alunoSorteado==2:
    alunoSorteadoNome = nome2

if alunoSorteado==3:
    alunoSorteadoNome = nome3

if alunoSorteado==4:
    alunoSorteadoNome = nome4

print(f'O aluno {alunoSorteadoNome} foi sorteado')
