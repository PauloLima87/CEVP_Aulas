print(f'{"Listas podem ser modificadas":=^45}')
lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print(lanche)
lanche[3] = 'picolé'
print(lanche)
num = [2, 5, 9, 1]
print(num)

print(f'\n\n{"Adicionando um elemento a lista":=^45}')
print(f'\n{"==Append: add fim da lista":=<30}')
lanche.append('cookie')
print(lanche)
print(f'\n{"==COM NUMEROS":=<20}')
num.append(7)
print(num)

print(f'\n{"==Insert: add na posição":=<30}')
lanche.insert(0, 'cachorro quente')
print(lanche)
print(f'\n{"==COM NUMEROS":=<20}')
num.insert(2, 0)
print(num)

print(f'\n\n{"Removendo um elemento a lista":=^45}')
print(f'\n{"==DEL":=<30}')
del lanche[3]  # elimina pizza pela chave e reposiciona a lista
print(lanche)
print(f'\n{"==POP":=<30}')
lanche.pop(3)  # elimina picolé pela chave e reposiciona a lista
# lanche.pop() elimina o ultimo elemento
print(lanche)

print(f'\n{"==REMOVE":=<30}')
lanche.remove('suco')  # elimina suco pelo valor e reposiciona a lista
print(lanche)  # em caso de termos iguais remove elimina a primeira ocorrencia de 'suco'

print(f'\n\n{"Criando e manipulando uma lista":=^45}')

print(f'\n{"==list(range(4, 11))":=<30}')
valores = list(range(4, 11))  # cria uma lista com os valores de 4 a 10 já ordenados
print(valores)

print(f'\n{"==MANIPULANDO":=<30}')
valores = [8, 2, 5, 4, 9, 3, 0]
print(valores)
valores.sort()
print(f'\n{"==ordenação crescente":=<30}')
print(valores)

valores.sort(reverse=True)
print(f'\n{"==ordenação decrescente":=<30}')
print(valores)

print(f'\n{"==len(valores)":=<30}')
print(f'A lista possui {len(valores)} valores')

print(f'\n{"==apresentando resultado":=<30}')

exe2 = list()
exe2.append(5)
exe2.append(9)
exe2.append(4)
print(exe2)
for v in exe2:
    print(f'{v}...', end='')

print('\n')
for s, v in enumerate(exe2):  # 's' equivale ao indice do numero 'v' a ser apresentado
    print(f'{s} - {v}')

"""print(f'\n{"==lendo valores da lista":=<30}')
exe3 = list()
for con in range(0, 5):
    exe3.append(int(input(f'Valor {con}: ')))
print(exe3)"""

print(f'\n{"==OBSERVAÇÕES":=<30}')
a = [2, 3, 4, 7]
b = a # o Python faz uma LIGAÇÂO entre 'a' e 'b'
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'\nAo alterar "b" consequentemente "a" tbm será alterado: ex b[2] = 8')
b[2] = 8
print(f'NOVA Lista A: {a}')
print(f'NOVA Lista B: {b}')
print(f"""\npara que "b" receba uma cópia de "a" fazemos por fatiamento b = a[:]
Logo podemos alterar "b" sem modificar "a". Ex b[2]= 4""")
b= a[:]
b[2] = 4
print(f'Lista A: {a}')
print(f'Lista B: {b}')