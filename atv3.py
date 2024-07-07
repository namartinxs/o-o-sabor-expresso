class Musica:
    def __init__(self,nome,artista,duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
    def __str__(self) -> str:
        return f' {self.nome} de {self.artista} com duração de {self.duracao} minutos.'
    
   

first_place = Musica('Palavras no corpo','Gal Costa',4)
second_place = Musica('Cabide','Mart\'nália',3)
third_place = Musica('Ovelha Negra','Rita Lee', 8)

print(f'''AS MAIS OUVIDAS ESTA SEMANA
      1º LUGAR: {first_place}
      2º LUGAR: {second_place}
      3º LUGAR: {third_place}
      ''')
