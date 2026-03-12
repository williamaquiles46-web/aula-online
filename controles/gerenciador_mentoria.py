class GerenciadorMentoria:
    def __init__(self):
        self.__mentorias = []

    def cadastrarMentoria(self, mentoria):
        self.__mentorias.append(mentoria)
        print("Mentoria cadastrada com sucesso!")

    def listarMentorias(self):
        if not self.__mentorias:
            print("⚠ Nenhuma mentoria cadastrada.")
        else:
            print("Lista de mentorias:")
            for m in self.__mentorias:
                m.imprime()

    def buscarMentoriaPorEstudante(self, estudante):
        resultado = [m for m in self.__mentorias if m.getEstudante() == estudante]
        if not resultado:
            print(f"Nenhuma mentoria encontrada para {estudante.getNome()}.")
        else:
            print(f"Mentorias de {estudante.getNome()}:")
            for m in resultado:
                m.imprime()

    def removerMentoria(self, mentoria):
        if mentoria in self.__mentorias:
            self.__mentorias.remove(mentoria)
            print("✅ Mentoria removida com sucesso!")
        else:
            print("⚠ Mentoria não encontrada.")

    def getMentorias(self):
        return self.__mentorias
