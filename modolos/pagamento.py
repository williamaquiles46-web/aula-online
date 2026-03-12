from modolos.estudante import Estudante
class Pagamento:
    def __init__(self, estudante, valor, status="pendente"):
        self.__estudante = estudante   
        self.__valor = valor           
        self.__status = status         

    def getEstudante(self):
        return self.__estudante
    
    def getValor(self):
        return self.__valor
    
    def getStatus(self):
        return self.__status

    def setStatus(self, novo_status):
        self.__status = novo_status

    def imprime(self):
        print(f"Estudante: {self.__estudante.getNome()}")
        print(f"Valor: R${self.__valor}")
        print(f"Status: {self.__status}")
