import justpy as jp
from controles.gerenciador_estudante import GerenciadorEstudante
from controles.gerenciador_professor import GerenciadorProfessor

ger_est = GerenciadorEstudante()
ger_prof = GerenciadorProfessor()

def listagem():
    wp = jp.WebPage()
    jp.H1(text="Listagem de Usuários", classes="text-2xl m-4", a=wp)

    jp.H2(text="Estudantes", classes="text-xl m-2", a=wp)
    for est in ger_est.getEstudantes():
        jp.Div(text=f"{est.getNome()} - {est.getEmail()}", classes="m-2 p-2 border", a=wp)

    jp.H2(text="Professores", classes="text-xl m-2", a=wp)
    for prof in ger_prof.getProfessores():
        jp.Div(text=f"{prof.getNome()} - {prof.getEmail()} ({prof.getEspecialidade()})", classes="m-2 p-2 border", a=wp)

    return wp

jp.justpy(listagem)
