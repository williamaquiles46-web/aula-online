from modolos.exercicio import Exercicio
from modolos.estudante import Estudante
class Avaliacao:
    def __init__(self, estudante, exercicio, nota, comentario = ""):
        self.__estudante = estudante       
        self.__exercicio = exercicio       
        self.__nota = nota                 
        self.__comentario = comentario 

    def getEstudante(self):
        return self.__estudante
    
    def getExercicio(self):
        return self.__exercicio
    
    def getNota(self):
        return self.__nota
    
    def getComentario(self):
        return self.__comentario   
        

    def setNota(self, nova_nota):
        self.__nota = nova_nota
    
    def setComentario(self, novo_comentario):
        self.__comentario = novo_comentario    


    def imprime(self):
        print(f"Estudante: {self.__estudante.getNome()}")
        print(f"Exercício: {self.__exercicio.getDescricao()}")
        print(f"Nota: {self.__nota}")
        print(f"Comentário: {self.__comentario}")    