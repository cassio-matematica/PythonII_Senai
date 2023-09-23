"""conta={"nome": "Cássio", "cpf":111111111, "Saldo":1000, "Limite":10000}

def saldo():
    print(conta["Saldo"])

def deposito(valor_deposito):
     conta["Saldo"]= conta["Saldo"]+ valor_deposito

def saque(valor_saque):
     conta["Saldo"]= conta["Saldo"]- valor_saque

print(conta)
saldo()
deposito(200)
saque(100)
saldo()"""

# conta.py

class Conta:
    def __init__(self, nome, cpf, saldo, limite):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo
        self.limite = limite

    def consultar_saldo(self):
        print(f"Saldo atual da conta de {self.nome}: R${self.saldo:.2f}")

    def depositar(self, valor_deposito):
        self.saldo += valor_deposito
        print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso.")

    def sacar(self, valor_saque):
        if self.saldo >= valor_saque:
            self.saldo -= valor_saque
            print(f"Saque de R${valor_saque:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente para o saque.")





    




