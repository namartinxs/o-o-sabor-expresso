# Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante
class Restaurante:
    def __init__(self,nome,categoria,aluguel,alvara = False,ativo = False):
        
        self.nome =nome 
        self.categoria = categoria
        self.aluguel = aluguel 
        self.alvara = alvara 
        self.ativo = ativo
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
        
rest_modelo_formatado = Restaurante('Albatroz','massas')
print(rest_modelo_formatado)
