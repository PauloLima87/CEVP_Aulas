for c in range(1, 6): #1 até 5 e para no 6 (5 VEZES)
    print('oi')
print('FIM\n')

for c in range(0, 6): #0 até 5 e para no 6 (6 VEZES)
    print('olá')
print('FIM\n')

for c in range(1, 6): #1 até 5 e para no 6 (5 VEZES)
    print(c)
print('FIM\n')

for c in range(0, 6): #0 até 5 e para no 6 (6 VEZES)
    print(c)
print('FIM\n')

for c in range(1, 7): #0 até 5 e para no 6 (6 VEZES)
    print(c)
print('FIM\n')

for c in range(6, 0, -1): #6 até 1 regressiva (6 VEZES)
    print(c)
print('FIM\n')

for c in range(0, 7, 2): #0 até 7 e para no 6, com passo de 2 em 2(6 VEZES)
    print(c)
print('FIM\n')

for c in range(7, 0, -2): #0 até 7 e para no 6, com passo de 2 em 2(6 VEZES)
    print(c)
print('FIM\n')

#CONATGEM de 0 a N
n = int(input('Numero: '))
for c in range(0, n+1):
    print(c)
print('FIM\n')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM\n')

for c in range(0,3):
    n = int(input('Valor: '))
print(n) #N não armazena todos os valores, apenas o ultimo
print('FIM\n')

s = 0
for c in range(0, 4):
    n = int(input('Valor: '))
    s += n
print(s) #N não armazena todos os valores, apenas o ultimo
print('FIM\n')
