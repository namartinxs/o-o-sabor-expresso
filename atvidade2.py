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
  

# #Crie duas instâncias da classe e imprima essas instâncias
# instan1 = ContaBancaria('Ana', 1200)
# instan2 = ContaBancaria('Paulo', 2300)
# print(instan1)
# print(instan2)
# # Crie uma instância da classe, chame o método de classe e imprima o valor de ativo
# instan3 = ContaBancaria('João',1800)
# print(f'Antes de ativar a conta {instan3._ativo}')
# ContaBancaria.ativar_conta(instan3)
# print(f'Depois de ativar a conta{instan3._ativo}')

# Refatore a classe `ContaBancaria` para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.
class ContaBancariaRefatorada:
    def __init__(self,titular,saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False


    @property  
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self._ativo
  

# Crie uma instância da classe e imprima o valor da propriedade titular.
#inst4 = ContaBancariaRefatorada("Ana", 45000)
#print(f"TITULAR: {inst4.titular}")



# Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
class ClienteBanco:
    def __init__(self, nome, endereco, idade, saldo, credito):
        self.nome = nome
        self.endereco = endereco
        self.idade = idade
        self.saldo = saldo
        self._credito = credito

    @classmethod
    def credito_especial(cls, nome, endereco, idade, saldo):
        # Adiciona crédito especial para idosos (idade > 60)
        if idade > 60:
            credito_especial = 500.0
        else:
            credito_especial = 0.0
        
        # Adiciona crédito adicional baseado no saldo inicial
        credito_adicional = saldo * 0.1
        
        # Calcula o crédito total
        credito_total = credito_especial + credito_adicional
        
        # Cria e retorna a instância do cliente
        return cls(nome, endereco, idade, saldo, credito_total)

# Exemplo de uso
cliente = ClienteBanco.credito_especial("João Silva", "Rua Exemplo, 123", 65, 1000.0)
print(f"Nome: {cliente.nome}, Endereço: {cliente.endereco}, Idade: {cliente.idade}, Saldo: {cliente.saldo}, Crédito: {cliente._credito}")

