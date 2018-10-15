for c in range(1, 10):
    print(c, end=':')
print(' FIM FOR')

c = 1
while c < 10:
    print(c, end=':')
    c += 1
print(' FIM WHILE')

for c in range(1, 3):
    n = int(input('Digite um valor: '))
print('FIM FOR')

c = 1
while c != 0:
    c = int(input('Digite um valor'))
print('FIM WHILE')
r = 'S'
while r == "S":
    c = int(input('Digite um valor'))
    r = str(input('Deseja continuar? [s/n]')).upper()
print('FIM WHILE')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Nº: '))
    if n != 0:
        if n % 2 == 0:
            par+=1
        else:
            impar+=1
print(f"""{par} Nºs pares
{impar} Nºs Impares""")
