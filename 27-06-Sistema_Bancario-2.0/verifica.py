import time

class Banco:
    def __init__(self):
        self.limite_saque = 3
        self.contagens_saques = 0
        self.limite_valor_saque = 500.00
        self.extrato = ""
        self.saldo = 0

    def day(self, mes):
        print("Mês", mes, end="", flush=True)
        for i in range(3):
            time.sleep(0.3)
            print(".", end="", flush=True)

    def deposito(self):
        a = float(input("Digite o seu deposito: R$"))
        if a > 0:
            self.saldo += a
            self.extrato += f"\nDeposito: R${a:.2f} "
            print(f"Depósito realizado com sucesso! Novo saldo: R${self.saldo:.2f}")
        else:
            print("O valor de deposito é inválido!")

    def saque(self):
        if self.contagens_saques >= self.limite_saque:
            print("Limite diário de saques atingido.")
            return

        b = float(input("Digite o valor que deseja sacar R$"))

        if b > self.limite_valor_saque:
            print("Valor do saque excede o limite permitido.")
        elif b > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= b
            self.extrato += f"\nSaque: R${b:.2f} "
            self.contagens_saques += 1
            print(f"Saque realizado com sucesso! Novo saldo: R${self.saldo:.2f}")

    def mostrar_extrato(self):
        print("----------Extrato----------")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
