class Mentoria:
    def __init__(self, professor, estudante, tema, duracao):
        self.__professor = professor   
        self.__estudante = estudante   
        self.__tema = tema
        self.__duracao = duracao       

    def getProfessor(self):
        return self.__professor
    
    def getEstudante(self):
        return self.__estudante
    
    def getTema(self):
        return self.__tema
    
    def getDuracao(self):
        return self.__duracao

    def imprime(self):
        print(f"Mentoria sobre: {self.__tema}")
        print(f"Professor: {self.__professor.getNome()}")
        print(f"Estudante: {self.__estudante.getNome()}")
        print(f"Duração: {self.__duracao} minutos")