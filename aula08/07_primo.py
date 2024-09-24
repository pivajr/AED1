numero = 0
while (numero <= 0):
    numero = int(input('Digite o número a ser verificado: '))
    if (numero <= 0):
        print('O numero deve ser positivo!')

primo = True
for i in range(2, int(numero / 2) + 1):
    if (numero % i == 0):
        primo = False

if (primo):
    print('O número é primo')
else:
    print('O número nao é primo')
