class Pessoa:
    def __init__(self,nome, idade, profissao):
        self.nome=nome
        self.idade=idade
        self.profissao=profissao

    def __str__(self):
        return f'NOME {self.nome} | IDADE {self.idade} | PROFISSÃO {self.profissão}'
    
    def aniversário(self):
        self.idade += 1

    @property
    def saudacao(self):
        return f'Olá,{self.nome}! Parabéns pelo dia do {self.profissao}.'
    