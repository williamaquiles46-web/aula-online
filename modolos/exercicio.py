
class Exercicio:
    def __init__(self, descricao, dificuldade, resposta_correta):
        self.__descricao = descricao
        self.__dificuldade = dificuldade
        self.__resposta_correta = resposta_correta
        self.__tentativas = []

    def getDescricao(self): return self.__descricao
    def getDificuldade(self): return self.__dificuldade
    def getResposta_correta(self): return self.__resposat_correta
    def getTentativas(self): return self.__tentativas

    def setDescricao(self, nova_descricao):
        self.__descricao = nova_descricao
    
    def setDificuldade(self, nova_dificuldade):
        self.__dificuldade = nova_dificuldade
    
    def setRespostaCorreta(self, nova_resposta):
        self.__resposta_correta = nova_resposta

    def responder(self, resposta_estudante):
        self.__tentativas.append(resposta_estudante)
        return resposta_estudante == self.__resposta_correta

    def imprime(self):
        print(f"Descrição: {self.__descricao}")
        print(f"Dificuldade: {self.__dificuldade}")
        print(f"Tentativas: {self.__tentativas}")   