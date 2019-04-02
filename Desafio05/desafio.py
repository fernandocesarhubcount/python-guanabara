inteiro = input('Digite um valor inteiro: ')

if inteiro.isnumeric():
    inteiro = int(inteiro)
    print('O valor é {}. Seu antecessor é {} e seu sucessor é o {}'.format(inteiro, inteiro-1, inteiro+1))
else:
    print('O valor não é um número inteiro!')