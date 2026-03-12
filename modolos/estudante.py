from modolos.exercicio import Exercicio
from modolos.pessoa import Pessoa
class Estudante(Pessoa):
    def __init__(self, nome, email, matricula):
        super().__init__(nome, email)
        self.__matricula = matricula
        self.__horas_cursadas = []
        self.__exercicios_respondidos = []

    def getMatricula(self): return self.__matricula
    def setMatricula(self, m): self.__matricula = m   
    def getHoras_cursadas(self): return self.__horas_cursadas
    def setHorasCursadas(self, h): return self.__horas_cursadas.append(h)

    def adicionarExercícioRealizado(self, exercicio, resposta ):
         resultado = exercicio.responder(resposta)
         self.__exercicios_respondidos.append((exercicio, resposta, resultado))
         return resultado
    
    def getExerciciosRealizados(self):
        return self.__exercicios_respondidos
    

    def imprime(self):
        super().imprime()
        print(f"Matrícula: {self.__matricula}")
        print(f"Horas cursadas: {self.__horas_cursadas}")
        print("Exercícios realizados:")
        for ex, resp, res in self.__exercicios_respondidos:
            print(f"- {ex.getDescricao()} | Resposta: {resp} | {'Correta' if res else 'Errada'}")