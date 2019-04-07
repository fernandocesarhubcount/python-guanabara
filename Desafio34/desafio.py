novoSalario = 0
salario = float(input('Digite o salário atual: '))

if salario>1250:
    novoSalario = salario * 1.1
else:
    novoSalario = salario * 1.15

print(f'O seu novo salário é de R$ {novoSalario:.2f} ({(novoSalario*100/salario)-100} % de reajuste)')