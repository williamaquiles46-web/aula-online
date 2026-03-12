from modolos.aula import Aula
from infra.excecoes import ItemNaoEncontradoError

class GerenciadorAula:
    def __init__(self):
        self.__lista_aulas = []

    def cadastrarAula(self, nova_aula):
        self.__lista_aulas.append(nova_aula)
        print("Aula cadastrada!")

    def listarAulas(self):
        if not self.__listar_aulas:
            print("Nenhuma aula cadastrada")
            return
        for aula in self.__lista_aulas:
            aula.imprime()
    def removerAula(self, nome_sala):
        for aula in self.__lista_aulas:
            if aula.getSala().lower() == nome_sala.lower():
                self.__lista_aulas.remove(aula)
                return True
        
        
        raise ItemNaoEncontradoError(f"A sala {nome_sala} não possui aula cadastrada.")

    def get_todas_aulas(self):
        return self.__lista_aulas                                