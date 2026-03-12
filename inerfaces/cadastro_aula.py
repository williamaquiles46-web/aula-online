import justpy as jp
from modolos.aula import Aula
from controles.gerenciador_aulas import GerenciadorAula
from controles.gerenciador_professor import GerenciadorProfessor

ger_aula = GerenciadorAula()
ger_prof = GerenciadorProfessor()

def cadastro_aula():
    wp = jp.WebPage()
    jp.H1(text="Cadastro de Aula", classes="text-2xl m-4", a=wp)

    nome = jp.Input(placeholder="Nome da aula", classes="m-2 p-2 border", a=wp)
    duracao = jp.Input(placeholder="Duração (minutos)", classes="m-2 p-2 border", a=wp)
    prof_nome = jp.Input(placeholder="Nome do professor", classes="m-2 p-2 border", a=wp)

    msg = jp.Div(classes="m-2 p-2 text-green-600", a=wp)

    def cadastrar(btn, msg=msg):
        prof = next((p for p in ger_prof.getProfessores() if p.getNome().lower() == prof_nome.value.lower()), None)
        if prof:
            aula = Aula(nome.value, prof, int(duracao.value))
            ger_aula.cadastrarAula(aula)
            msg.text = f"✅ Aula {aula.getNome()} cadastrada!"
        else:
            msg.text = "⚠ Professor não encontrado."

    jp.Button(text="Cadastrar", classes="bg-blue-500 text-white m-2 p-2", a=wp, click=cadastrar)
    return wp

jp.justpy(cadastro_aula)
