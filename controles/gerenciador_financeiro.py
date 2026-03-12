from modolos.pagamento import Pagamento

class GerenciadorFinanceiro:
    def __init__(self):
        self.__pagamentos = []

    def registrarPagamento(self, pagamento):
        self.__pagamentos.append(pagamento)
        print("Pagamento registrado com sucesso!")

    def listarPagamentos(self):
        if not self.__pagamentos:
            print("Nenhum pagamento registrado.")
        else:
            print("Lista de pagamentos:")
            for p in self.__pagamentos:
                p.imprime()

    def buscarPagamentosPorEstudante(self, estudante):
        resultado = [p for p in self.__pagamentos if p.getEstudante() == estudante]
        if not resultado:
            print(f"Nenhum pagamento encontrado para {estudante.getNome()}.")
        else:
            print(f"Pagamentos de {estudante.getNome()}:")
            for p in resultado:
                p.imprime()

    def removerPagamento(self, pagamento):
        if pagamento in self.__pagamentos:
            self.__pagamentos.remove(pagamento)
            print("Pagamento removido com sucesso!")
        else:
            print("Pagamento não encontrado.")

    def getPagamentos(self):
        return self.__pagamentos
