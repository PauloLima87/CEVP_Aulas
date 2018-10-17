cont = 1
while cont <= 10:
    print(cont, ' ...', end='')
    cont += 1
print('Acabou')

#while True:
#    print(cont, ' ...', end='')
#    cont += 1
#print('Acabou')

n = s = s2 =0
while n != 999:
    n = int(input('nº: '))
    s += n
print(f'Soma é {s}')

while True:
    n = int(input('nº: '))
    if n ==999:
        break
    s2+=n
print(f'Soma 2 : {s2}')