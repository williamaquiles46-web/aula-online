class Pessoa:

    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email

    def getNome(self):
        return self.__nome
    def getEmail(self):
        return self.__email
    
    def setNome(self, novoNome):
        self.__nome = novoNome
    def setEmail(self, novoEmail):
        self.__email = novoEmail

    def imprime(self):
        print("Nome: ", self.__nome)
        print("Email: ", self.__email)
