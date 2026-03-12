from modolos.professor import Professor

class GerenciadorProfessor:
    def __init__(self):
        self.__professores = []

    def cadastrarProfessor(self, professor):
        self.__professores.append(professor)
        print("Professor cadastrado com sucesso!")

    def listarProfessores(self):
        if not self.__professores:
            print("Nenhum professor cadastrado.")
        else:
            print("Lista de professores:")
            for prof in self.__professores:
                prof.imprime()

    def buscarProfessorPorNome(self, nome):
        resultado = [prof for prof in self.__professores if prof.getNome().lower() == nome.lower()]
        if not resultado:
            print(f"Nenhum professor {nome} encontrado.")
        else:
            print(f"Professor {nome} encontrado")
            for prof in resultado:
                prof.imprime()

    def removerProfessor(self, professor):
        encontrada = False
        for prof in self.__professores:
            if prof == professor:  
                self.__professores.remove(prof)
                encontrada = True
                print(f"Professor {prof.getNome()} removido com sucesso!")
                break
        if encontrada == False:
            print("Professor não encontrado.")

    def getProfessores(self):
        return self.__professores
