print(f"""{'Tuplas':-^35}""")
print(f'{"Tuplas são Imutáveis":^35}')
print(f'{"É possivel deletar a tupla com del(a)":^35}')
print(f'{"Não é possivel deletar termo da tupla com del(a[0])":^35}')

print('-' * 35)

lanche = ('Hamburguer', 'suco', 'pizza', 'pudim')  # criando uma tupla
lanche2 = 'sanduiche', 'refrigerante', 'coxinha', 'sorvete'  # tambem é uma tupla
for c in lanche:
    print(c)

print(f'1- {lanche}')
print(f'2- {lanche2}')
print(f'3 - Lanche[1]: {lanche[1]}')

# FATIAMENTO EM TUPLAS
print(f'4 - Lanche[1:3]: {lanche[1:3]}')  # fatiamento na tupla
print(f'5 - Lanche[2:]: {lanche[2:]}')
print(f'6 - Lanche[:2]: {lanche[:2]}')
print(f'7 - Lanche[-2]: {lanche[-2]}')  # contagem de tras pra frente
print(f'8 - Lanche[-2:]: {lanche[-2:]}')  # contagem de tras pra frente, percorrendo até o final

print(f'\n{"UTILIZANDO FOR":=^35}')

# QDO POSIÇÂO NAO È NECESSÀRIA
for comida in lanche2:
    print(f'\n...{comida}')
print("\n")

# QDO ALEM DO CONTEUDO È PRECISO PRINTAR A POSIÇÂO
# FORMA 1
for comida in range(0, len(lanche2)):
    print(f'Comida: {comida}')  # mostra indices
    print(f'Comida: {lanche2[comida]}\n')  # mostra o conteúdo

# FORMA 2
for pos, comida in enumerate(lanche2):
    print(f'Vou comer {comida} na posição {pos}')

print(f'\n{"UTILIZANDO SORTED":=^35}')
print(f'\n{"sorted apenas reorganiza a apresentação"}')
print(f'\n{"não modifica o conteudo da tupla"}')

print(f'Sorted ', sorted(lanche2))  # Apresenta como uma lista
print(f'Tupla ', lanche2)

print(f'\n{"CONCATENANDO":=^35}')
a = (2, 5, 4)
b = (5, 8, 1, 2)
print('A = : ', a)
print('B = : ', b)
c = a + b
print('A + B =',c)
c = b + a
print('B + A =',c)

print(f'\n{"METODOS UTEIS":=^35}')
print('Verifica existencia de termo em C (num 5): ', c.count(5))
print('Verifica existencia de termo em C (num 9): ', c.count(9))
print('Em que posição está o termo 5 em C: ', c.index(5)) #Apresenta apenas a primaira ocorrnecia
print('Em que posição está o segundo termo 5 em C: ', c.index(5, 1)) #Busca uma ocorencia a partir do indice 1, ignorando a primeira ocorrenci do 5 em 0
print('Em que posição está o termo 8 em C: ', c.index(8))
#print('Em que posição está o termo 9 em C: ', c.index(9)) #se nao existe ele apresents ERRO e não apresenta o print

print(f'\n{"DADOS DE TIPOS DIFERENTES":=^35}')
pessoa = ('Paulo', 39, 'M', 122.8)
print(pessoa)
