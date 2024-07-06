class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurante_pizaa = Restaurante()

restaurantes =[restaurante_pizaa,restaurante_praca]
print(dir(restaurante_praca))