class Horario:

    def __init__(self, dia, horarioInicial, horarioFinal):
        self.__dia = dia
        self.__horarioInicial = horarioInicial
        self.__horarioFinal = horarioFinal

    def getDia(self):
        return self.__dia
    def getHorarioInicial(self):
        return self.__horarioInicial
    def getHorarioFinal(self):
        return self.__horarioFinal
    
    def setDia(self, novoDia):
        self.__dia = novoDia
    def setHorarioInicial(self, novohorarioInicial):
        self.__horarioInicial = novohorarioInicial
    def setHorarioFinal(self, novohorarioFinal):
        self.__horarioFinal = novohorarioFinal

    def imprime(self):
        print("Dia: ", self.__dia)
        print("Horário inicial: ", self.__horarioInicial)
        print("Horário final: ", self.__horarioFinal)