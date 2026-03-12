from modolos.exercicio import Exercicio
class GerenciadorExercicio:
    def __init__(self):
        self.__exercicios = []

    def cadastrarExercicio(self, exer): 
        self.__exercicios.append(exer)
        print("Exercício cadastrado com sucesso!")

    def removerExercicio(self, descricao_exercicio):
        for exercicio in self.__exercicios:
            if exercicio.getDescricao().lower() == descricao_exercicio.lower():
                self.__exercicios.remove(exercicio)
                return True
        return False

    def listar_exercicios(self):
        return self.__exercicios

    def getExercicios(self):
        return self.__exercicios
        
