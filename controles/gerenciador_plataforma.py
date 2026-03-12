from controles.gerenciador_estudante import GerenciadorEstudante
from controles.gerenciador_professor import GerenciadorProfessor
from controles.gerenciador_aulas import GerenciadorAula
from controles.gerenciador_exercicios import GerenciadorExercicio
from controles.gerenciador_avaliacao import GerenciadorAvaliacao
from controles.gerenciador_mentoria import GerenciadorMentoria
from controles.gerenciador_financeiro import GerenciadorFinanceiro

class GerenciadorPlataforma:
    def __init__(self):
        self.__estudantes = GerenciadorEstudante()
        self.__professores = GerenciadorProfessor()
        self.__aulas = GerenciadorAula()
        self.__exercicios = GerenciadorExercicio()
        self.__avaliacoes = GerenciadorAvaliacao()
        self.__mentorias = GerenciadorMentoria()
        self.__financeiro = GerenciadorFinanceiro()

    def getGerenciadorEstudante(self):
        return self.__estudantes

    def getGerenciadorProfessor(self):
        return self.__professores

    def getGerenciadorAula(self):
        return self.__aulas

    def getGerenciadorExercicio(self):
        return self.__exercicios

    def getGerenciadorAvaliacao(self):
        return self.__avaliacoes

    def getGerenciadorMentoria(self):
        return self.__mentorias

    def getGerenciadorFinanceiro(self):
        return self.__financeiro
