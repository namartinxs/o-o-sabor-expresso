# Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
class ContaBancaria:
 def __init__(self,titular,saldo):
  self.titular = titular
  self.saldo = saldo
  self._ativo = False

    # Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. .
 def __str__(self):
  return f'TITULAR DA CONTA {self.titular} SALDO DA CONTA {self.saldo}'
 # Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. 
 @classmethod
 def ativar_conta(cls,conta):
   conta._ativo = True
  

#Crie duas instâncias da classe e imprima essas instâncias
instan1 = ContaBancaria('Ana', 1200)
instan2 = ContaBancaria('Paulo', 2300)
print(instan1)
print(instan2)
# Crie uma instância da classe, chame o método de classe e imprima o valor de ativo
instan3 = ContaBancaria('João',1800)
print(f'Antes de ativar a conta {instan3._ativo}')
ContaBancaria.ativar_conta(instan3)
print(f'Depois de ativar a conta{instan3._ativo}')




