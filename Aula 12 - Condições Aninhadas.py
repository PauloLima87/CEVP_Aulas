nome = str(input('Qual se nome: ')).strip().capitalize()
if nome =="Paulo":
    print('que nome bonito!')
elif nome =='Pedro' or nome == 'Maria' or nome == 'João':
    print('Seu nome é muito popular no Brasil')
elif nome in 'Paula Rebeca Juliana Flavia':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')
print(f'Olá! {nome}')