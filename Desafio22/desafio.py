nome = input('Digite o nome da pessoa: ')

#Maiusculas
print(nome.upper())

#Minusculas
print(nome.lower())

#Total letras s/ espaço
print(len(nome)-nome.count(' '))

#Total letras primeiro nome
print(len(nome.split()[0]))
print(len(nome.find(' ')))