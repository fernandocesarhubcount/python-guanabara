isTriangulo = False
lados = 1
valor = 0
valores = []

while lados<4:
    valor = float(input('Digite o valor da reta: '))
    valores.append(valor)
    lados+=1

if valores[0] < valores[1]+valores[2] and valores[1] < valores[2]+valores[0] and valores[2] < valores[1]+valores[0]:
    if valores[0]>abs(valores[1]-valores[2]) and valores[1]>abs(valores[0]-valores[2]) and valores[2]>abs(valores[0]-valores[1]):
        isTriangulo = True

print(f'As 3 retas{"" if isTriangulo else " não"} podem formar um triãngulo!')

