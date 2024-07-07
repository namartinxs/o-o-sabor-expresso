
# Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
class Restaurante:
    def __init__(self,nome,categoria,aluguel,alvara = False,ativo = False):
        
        self.nome =nome 
        self.categoria = categoria
        self.aluguel = aluguel 
        self.alvara = alvara 
        self.ativo = ativo
        
rest_modelo = Restaurante('Albatroz','massas')
