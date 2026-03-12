from modolos.professor import Professor
from modolos.horario import Horario
class Aula:

    def __init__(self, professor, horario, sala, capacidade):
        if capacidade <= 0:
            raise ValueError("Capacidade deve ser maior que zero.")
        self.__professor = professor
        self.__horario = horario
        self.__sala = sala
        self.__capacidade = capacidade

    def getProfessor(self):
        return self.__professor
    def getHorario(self):
        return self.__horario
    def getSala(self):
        return self.__sala
    def getCapacidade(self):
        return self.__capacidade
    
    def imprime(self):
        print("DADOS DA AULA:")
        print("Professor:")
        self.__professor.imprime()
        print("Horário:")
        self.__horario.imprime()
        print("Sala: ", self.__sala)
        print("Capacidade da sala: ", self.__capacidade)