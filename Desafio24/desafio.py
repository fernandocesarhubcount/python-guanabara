nomeCidade = input('Digite o nome da sua cidade: ').upper()

if nomeCidade.split()[0].find('SANTO') == 0:
    print('O nome da sua cidade começa com santo')
else:
    print('O nome da sua cidade não começa com santo')
