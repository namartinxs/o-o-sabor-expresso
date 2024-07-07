
# Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
class Restaurante:
    def __init__(self,nome,categoria,aluguel,ativo,alvara):
        
        self.nome =nome 
        self.categoria = categoria
        self.aluguel = aluguel 
        self.ativo = ativo
        self.alvara = alvara 
        
        
rest_modelo = Restaurante('Albatroz','massas',1200,True,True)
