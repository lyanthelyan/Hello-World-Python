# Crie uma classe chamada Círculo que tenha um atributo de instância chamado raio e dois métodos chamados calcular_area e calcular_circunferencia. O método calcular_area deve calcular a área do círculo (π * raio²) e o método calcular_circunferencia deve calcular a circunferência do círculo (2 * π * raio).
# import math
# class Circulo:
#     pi = (math.pi)
#     def __init__(self, raio):
#         self.raio = raio
    
#     def calcular_area(self):
#         return Circulo.pi * self.raio**2

#     def calcular_circunferencia(self):
#         return 2 * Circulo.pi * self.raio
    

# circulo1 = Circulo(3)
# print(circulo1.calcular_area())
        
        

#------------------------------------------------------------

# Crie uma classe chamada ContaBancaria que tenha os seguintes atributos: saldo (inicializado como 0) e titular (nome do titular da conta). A classe deve ter métodos para depositar dinheiro (depositar) e para sacar dinheiro (sacar). O método sacar deve verificar se há saldo suficiente antes de efetuar o saque.

class ContaBancaria:
    def __init__(self, titular):
        self.saldo = 0
        self.titular = titular

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor} realizado. Saldo atual: {self.saldo}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de {valor} realizado. Saldo atual: {self.saldo}")
        else:
            print("Saldo insuficiente. Saque não realizado.")

# Exemplo de uso da classe ContaBancaria
conta = ContaBancaria("João")  # Cria uma conta bancária com titular "João"
conta.depositar(500)  # Deposita 500 na conta
conta.sacar(200)  # Tenta sacar 200 da conta
conta.sacar(400)  # Tenta sacar 400 da conta
