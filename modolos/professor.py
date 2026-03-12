from modolos.pessoa import Pessoa

class Professor(Pessoa):

    def __init__(self, nome, email, matricula, disciplina, departamento):
        super().__init__(nome, email)
        self.__matricula = matricula
        self.__disciplina = disciplina
        self.__departamento = departamento

    def getMatricula(self):
        return self.__matricula
    def getDisciplina(self):
        return self.__disciplina
    def getDepartamento(self):
        return self.__departamento
    
    def setMatricula(self, novaMatricula):
        self.__matricula = novaMatricula
    def setDisciplina(self, novaDisciplina):
        self.__disciplina = novaDisciplina
    def setDepartamento(self, novoDepartamento):
        self.__departamento = novoDepartamento

    def imprime(self):
        super().imprime()
        print("Matrícula: ", self.__matricula)
        print("Disciplina: ", self.__disciplina)
        print("Departamento: ", self.__departamento)