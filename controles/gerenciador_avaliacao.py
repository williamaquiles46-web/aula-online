from modolos.estudante import Estudante
from modolos.exercicio import Exercicio
from modolos.avaliacao import Avaliacao
class GerenciadorAvaliacao:
    def __init__(self):
        self.__avaliacoes = []

    def cadastrarAvaliacoes(self, ava):
        self.__avaliacoes.append(ava)
        print("Avaliação cadastrada com sucesso!") 

    def removerAvaliacao(self, criterio):
        encontrada = False
        for a in self.__avaliacoes:
                if isinstance(criterio, Estudante) and a.getEstudante() == criterio:
                    self.__avaliacoes.remove(a)
                    encontrada = True
                    print(f"Avaliação de {criterio.getNome()} removida com sucesso!")
                    break
                elif isinstance(criterio, Exercicio) and a.getExercicio() == criterio:
                    self.__avaliacoes.remove(a)
                    encontrada = True
                    print(f"Avaliação do exercício '{criterio.getDescricao()}' removida com sucesso!")
                    break

        if not encontrada:
            print("Nenhuma avaliação encontrada para o critério informado.")


    def listar_avaliacoes(self):
        if not self.__avaliacoes:
            print("Não há avaliacoes cadastradas")
        else:
            for a in self.__avaliacoes:
                a.imprime()      


    def buscarAvaliacoesPorEstudante(self, estudante):
        resultado = [av for av in self.__avaliacoes if av.getEstudante() == estudante]
        if not resultado:
            print(f"⚠ Nenhuma avaliação encontrada para {estudante.getNome()}.")
        else:
            print(f"Avaliações de {estudante.getNome()}:")
            for av in resultado:
                av.imprime()            

    def getAvaliacoes(self):
        return self.__avaliacoes            
        