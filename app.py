#from arquivo                   classe
from modelos.restaurante import Restaurante

restaurante_paiol = Restaurante('paiol','caseiros')


restaurante_paiol.receber_avaliacao('Gui',10)
restaurante_paiol.receber_avaliacao('Ana',2)




def main ():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()