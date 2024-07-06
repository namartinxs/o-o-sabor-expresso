class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
#atribuir 
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'
#acessar
print(restaurante_praca.categoria)

if restaurante_praca.ativo == False:
    print(f'{restaurante_praca.nome} está inativo')
else:
    print(f'{restaurante_praca.nome} está ativo')

categoria = Restaurante.nome
print(categoria)

restaurante_praca.nome = 'Bistro'

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
if restaurante_pizza.categoria == 'Fast Food':
    print('CATEGORIA : FAST FOOD')
else:
    print('Esta não é a categoria do restaurante.')

restaurante_pizza.ativo = True

print(f'NOME:{restaurante_praca.nome}CATEGORIA:{restaurante_praca.categoria}')

