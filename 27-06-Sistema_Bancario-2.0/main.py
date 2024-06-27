from verifica import Banco

class ProgramaBancario:
    def __init__(self):
        self.banco = Banco()
        self.menu = ["d", "s", "e"]
        self.meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    def executar(self):
        print("Programa Bancário")
        print()

        for mes in self.meses:
            self.banco.day(mes)
            print("\n")

            opcao = input(f"Bem-Vindo! O que deseja fazer em seu banco? {self.menu} ").lower()
            print()

            if opcao in self.menu:
                if opcao == "d":
                    self.banco.deposito()
                elif opcao == "s":
                    self.banco.saque()
                elif opcao == "e":
                    self.banco.mostrar_extrato()
                else:
                    print("Operação inválida!")
            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    programa = ProgramaBancario()
    programa.executar()
