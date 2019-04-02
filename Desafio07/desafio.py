nota1 = ""
nota2 = ""
media = ""

while not nota1.isdigit():
    nota1 = input('Digite a primeira nota: ')

    if not nota1.isdigit():
        print('O valor não é um número')

while not nota2.isdigit():
    nota2 = input('Digite a segunda nota: ')

    if not nota2.isdigit():
        print('O valor não é um número')

media = (float(nota1)+float(nota2))/2

print('A média do aluno é igual a: {}'.format(media))