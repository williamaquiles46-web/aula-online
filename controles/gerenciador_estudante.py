from modolos.estudante import Estudante
from modolos.pessoa import Pessoa
class GerenciadorEstudante:
    def __init__(self):
        self.__lista_estudante = []

    def cadastrarEstudante(self, e):
        self.__lista_estudante.append(e)    
        print("Estudante cadastrado com sucesso!")

    def removerEstudante(self, estudante):
        encontrada = False
        for est in self.__lista_estudante:
            if est == estudante:   
                self.__lista_estudante.remove(est)
                encontrada = True
                print(f"Estudante {est.getNome()} removido com sucesso!")
                break
        if encontrada == False:
            print("Estudante não encontrado.")


    def listarEstudantes(self):
        if not self.__estudantes:
            print("Nenhum estudante cadastrado.")
        else:
            print("Lista de estudantes:")
            for est in self.__estudantes:
                est.imprime()

    def buscarEstudantePorNome(self, nome):
        resultado = [est for est in self.__estudantes if est.getNome().lower() == nome.lower()]
        if not resultado:
            print(f"Nenhum estudante encontrado com o nome {nome}.")
        else:
            print(f"Estudantes encontrados com o nome {nome}:")
            for est in resultado:
                est.imprime()         

    def getEstudantes(self):
        return self.__lista_estudante                  